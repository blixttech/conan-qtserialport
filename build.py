from cpt.packager import ConanMultiPackager
from cpt.ci_manager import CIManager
from cpt.printer import Printer
import re

if __name__ == "__main__":
    printer = Printer()
    ci_man = CIManager(printer)
    version = re.sub(".*/", "", ci_man.get_branch())
    builder = ConanMultiPackager(reference="qtserialport/%s" % version)
    builder.add_common_builds(pure_c=False)
    builder.run()
