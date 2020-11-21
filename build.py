from conans.client.conan_api import Conan
from cpt.packager import ConanMultiPackager, load_cf_class
from cpt.ci_manager import CIManager
from cpt.printer import Printer
import os, sys, re
import traceback

def hidesensitive(output):
    output_str = str(output)
    output_str = re.sub(r'(CONAN_LOGIN_USERNAME[_\w+]*)=\"(\w+)\"', r'\1="xxxxxxxx"', output_str)
    output_str = re.sub(r'(CONAN_PASSWORD[_\w+]*)=\"(\w+)\"', r'\1="xxxxxxxx"', output_str)
    sys.stdout.write(output_str)

def get_name_and_version():
    conan_api, _, _ = Conan.factory()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conanfile = load_cf_class(os.path.join(dir_path, "conanfile.py"), conan_api)
    name = conanfile.name
    version = conanfile.version

    if not version:
        printer = Printer(hidesensitive)
        ci_man = CIManager(printer)
        version = re.sub(".*/", "", ci_man.get_branch())

    return name, version

if __name__ == "__main__":
    try:
        builder = ConanMultiPackager(reference="%s/%s" % get_name_and_version(), out=hidesensitive)
        builder.add_common_builds()
        builder.run()
    except Exception as e:
        hidesensitive(traceback.format_exc())
        hidesensitive(str(e))
        sys.exit(1)
