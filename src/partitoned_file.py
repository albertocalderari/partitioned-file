from gzip import GzipFile

from core.partitioned_file_core import PartitionedFileCore


class PartitionedFile(PartitionedFileCore):
    def __init__(self, file_path, partition_size=64 * 1024 * 1024):
        super(PartitionedFile, self).__init__(file_path=file_path, partition_size=partition_size)

    def __enter__(self):
        file_handle = open(self.file_name, 'wb')
        self.set_file_handle(file_handle)
        return self


class PartitionedGzipFile(PartitionedFileCore):
    def __init__(self, file_path, partition_size=64 * 1024 * 1024):
        super(PartitionedFileCore, self).__init__(file_path, partition_size)
        self.file_path = file_path

    def __enter__(self):
        file_handle = GzipFile(fileobj=open(self.file_name, 'wb'), mode='wb')
        self.set_file_handle(file_handle)
        return self
