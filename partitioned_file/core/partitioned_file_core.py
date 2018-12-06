from file_with_size import FileWithSize


class PartitionedFileCore(object):
    def __init__(self, file_path, partition_size=64 * 1024 * 1024):
        self._file_path = file_path
        self._partition_size = partition_size
        self._idx = 0
        self._file_handle = None

    def write(self, payload):
        self._file_handle.write(payload)
        self._file_handle.flush()
        if self.is_greater_than_max_partition_size:
            self.close()
            self._idx += 1
            self.__enter__()

    @property
    def is_greater_than_max_partition_size(self):
        print self.file_handle.written_bytes
        return self.file_handle.written_bytes > self._partition_size

    @property
    def file_name(self):
        return self._file_path.replace('*', str(self._idx))

    @property
    def file_handle(self):
        return self._file_handle

    def open(self):
        return self.__enter__()

    def set_file_handle(self, handle):
        self._file_handle = FileWithSize(handle)

    def __enter__(self):
        raise NotImplemented("PartitionedFileCore is an interface!")

    def close(self):
        self.__exit__()

    def __exit__(self, *args, **kwargs):
        self._file_handle.close()

