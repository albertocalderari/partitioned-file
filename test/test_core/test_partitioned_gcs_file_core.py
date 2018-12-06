import unittest

from core.partitioned_gcs_file_core import PartitionedGCSFileCore


class TestPartitionedGCSFileCore(unittest.TestCase):
    def setUp(self):
        self.pf = PartitionedGCSFileCore("project_id", "bucket", "key/hello_*.txt")

    def test_gcs_full_path(self):
        actual = self.pf.gcs_full_path
        self.assertEqual(actual, "gs://bucket/key/hello_0.txt")
