from cpt.packager import ConanMultiPackager
from cpt.ci_manager import CIManager
from cpt.printer import Printer
import sys, re
import traceback

def hidesensitive(output):
    output_str = str(output)
    output_str = re.sub(r'(CONAN_LOGIN_USERNAME[_\w+]*)=\"(\w+)\"', r'\1="xxxxxxxx"', output_str)
    output_str = re.sub(r'(CONAN_PASSWORD[_\w+]*)=\"(\w+)\"', r'\1="xxxxxxxx"', output_str)
    sys.stdout.write(output_str)

if __name__ == "__main__":
    try:
        printer = Printer(hidesensitive)
        ci_man = CIManager(printer)
        version = re.sub(".*/", "", ci_man.get_branch())
        builder = ConanMultiPackager(reference=("qtserialport/%s" % version), out=hidesensitive)
        builder.add_common_builds(pure_c=False)
        builder.run()
    except Exception as e:
        hidesensitive(traceback.format_exc())
        hidesensitive(str(e))
        sys.exit(1)
