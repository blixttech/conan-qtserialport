from conans import ConanFile, tools
import re

class QtSerialPortConan(ConanFile):
    name = "qtserialport"
    description = "Serial port module for Qt"
    topics = ("conan", "qtserialport", "serialport")
    url = "https://github.com/blixttech/conan-qtserialport.git"
    homepage = "https://code.qt.io/cgit/qt/qtserialport.git"
    license = "LGPL-3.0"  # SPDX Identifiers https://spdx.org/licenses/

    python_requires = "qtmodulepyreq/0.1.0@blixt/stable"
    python_requires_extend = "qtmodulepyreq.QtModuleConanBase"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    """
    def set_version(self):
        git = tools.Git(folder=self.recipe_folder)
        version = re.sub(".*/", "", str(git.get_branch()))
        self.version = version
    """

    def requirements(self):
        self.requires("qt/%s@bincrafters/stable" % self.version)
