import unittest

from core.partitioned_file_core import PartitionedFileCore


class TestPartitionedFileCore(unittest.TestCase):
    def setUp(self):
        self.pf = PartitionedFileCore("hello_*.txt")

    def test_file_name(self):
        actual = self.pf.file_name
        self.assertEqual(actual, "hello_0.txt")


