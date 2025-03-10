"""
Created on Tue Jun 24 09:43:53 2014

@author: pietro
"""

from fnmatch import fnmatch
from io import BytesIO

from grass.gunittest.case import TestCase
from grass.gunittest.main import test

from grass.script.core import get_commands
from grass.exceptions import ParameterError
from grass.pygrass.modules.interface import Module


SKIP = [
    "g.parser",
]


class ModulesMeta(type):
    def __new__(cls, name, bases, dict):
        def gen_test(cmd):
            def test(self):
                Module(cmd)

            return test

        cmds = [
            c
            for c in sorted(list(get_commands()[0]))
            if c not in SKIP and not fnmatch(c, "g.gui.*")
        ]
        for cmd in cmds:
            test_name = "test__%s" % cmd.replace(".", "_")
            dict[test_name] = gen_test(cmd)
        return type.__new__(cls, name, bases, dict)


class TestModules(TestCase, metaclass=ModulesMeta):
    pass


class TestModulesPickability(TestCase):
    def test_rsun(self):
        """Test if a Module instance is pickable"""
        import pickle

        out = BytesIO()
        pickle.dump(Module("r.sun"), out)
        out.close()


class TestModulesCheck(TestCase):
    def test_flags_with_suppress_required(self):
        """Test if flags with suppress required are handle correctly"""
        gextension = Module("g.extension")
        # check if raise an error if required parameter are missing
        with self.assertRaises(ParameterError):
            gextension.check()

        # check if the flag suppress the required parameters
        gextension.flags.a = True
        self.assertIsNone(gextension.check())


if __name__ == "__main__":
    test()
