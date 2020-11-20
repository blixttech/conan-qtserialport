from cpt.packager import ConanMultiPackager
from cpt.ci_manager import CIManager
from cpt.printer import Printer

if __name__ == "__main__":
    printer = Printer()
    ci_man = CIManager(printer)
    builder = ConanMultiPackager(reference="qtserialport/%s" % ci_man.get_branch())
    builder.add_common_builds(pure_c=False)
    builder.run()
