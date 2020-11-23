from conans import ConanFile, tools
import re


class QtSerialPortConan(ConanFile):
    name = "qtserialport"
    description = "Serial port module for Qt"
    topics = ("conan", "qtserialport", "serialport")
    url = "https://github.com/blixttech/conan-qtserialport.git"
    homepage = "https://code.qt.io/cgit/qt/qtserialport.git"
    license = "LGPL-3.0"  # SPDX Identifiers https://spdx.org/licenses/

    python_requires = "qtmodulepyreq/0.1.0"
    python_requires_extend = "qtmodulepyreq.QtModuleConanBase"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    git_is_dirty = False
    git_commit = "unknown"

    def set_version(self):
        git = tools.Git(folder=self.recipe_folder)
        output = git.run("describe --all").splitlines()[0].strip()
        self.version = re.sub("^.*/v?", "", output)
        output = git.run("diff --stat").splitlines()
        self.git_is_dirty = True if output else False
        self.git_commit = git.run("rev-parse HEAD").splitlines()[0].strip()

        self.output.info("Version: %s, Commit: %s, Is_dirty: %s" %
                         (self.version, self.git_commit, self.git_is_dirty))
