import unittest

from core.partitioned_file_core import FileWithSize


class TestFileWithSize(unittest.TestCase):
    def setUp(self):
        self.pf = FileWithSize("")

    def test_n_bytes(self):
        actual = self.pf.n_bytes("jkl")
        self.assertEqual(3, actual)

    def test_increment_written_bytes(self):
        self.pf.increment_written_bytes("ab")
        self.assertEqual(self.pf.written_bytes, 2)
