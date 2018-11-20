from os.path import join

from partitioned_file_core import PartitionedFileCore


class PartitionedGCSFileCore(PartitionedFileCore):
    def __init__(self, project_id, bucket, file_path, partition_size=64 * 1024 * 1024):
        super(PartitionedGCSFileCore, self).__init__(file_path, partition_size)
        self.project_id = project_id
        self.bucket = bucket

    @property
    def gcs_full_path(self):
        return join('gs://' + self.bucket, self.file_name)
