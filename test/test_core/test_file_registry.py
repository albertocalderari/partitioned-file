import unittest

from core.file_registry import FileRegistry


class TestFileRegistry(unittest.TestCase):
    def test_add(self):
        fr = FileRegistry()
        fr.add("test")
        self.assertEqual(["test"], fr.items)

    def test__iter__(self):
        fr = FileRegistry(["t1", "t2"])
        expect = ["t1", "t2"]
        actual = [i for i in fr]
        self.assertEqual(expect, actual)