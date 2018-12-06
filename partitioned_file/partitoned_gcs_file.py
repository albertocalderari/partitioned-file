from gzip import GzipFile

import gcsfs

from core.partitioned_gcs_file_core import PartitionedGCSFileCore


class PartitionedGCSFile(PartitionedGCSFileCore):
    def __init__(self, project_id, bucket, file_path, partition_size=64 * 1024 * 1024):
        super(PartitionedGCSFile, self).__init__(project_id, bucket, file_path, partition_size)

    def __enter__(self):
        gcs_filesystem = gcsfs.GCSFileSystem(project=self.project_id)
        h = gcs_filesystem.open(self.gcs_full_path, 'wb')
        self.set_file_handle(h)
        self.add_file_to_registry()
        return self

    @classmethod
    def open(cls, project_id, bucket, file_path, partition_size=64 * 1024 * 1024):
        return cls(project_id, bucket, file_path, partition_size).__enter__()


class PartitionedGCSGzipFile(PartitionedGCSFileCore):
    def __init__(self, project_id, bucket, file_path, partition_size=64 * 1024 * 1024):
        super(PartitionedGCSGzipFile, self).__init__(project_id, bucket, file_path, partition_size)

    def __enter__(self):
        gcs_filesystem = gcsfs.GCSFileSystem(project=self.project_id)
        h1 = gcs_filesystem.open(self.gcs_full_path, 'wb')
        h = GzipFile(fileobj=h1, mode='wb')
        self.set_file_handle(h)
        self.add_file_to_registry()
        return self

    @classmethod
    def open(cls, project_id, bucket, file_path, partition_size=64 * 1024 * 1024):
        return cls(project_id, bucket, file_path, partition_size).__enter__()
