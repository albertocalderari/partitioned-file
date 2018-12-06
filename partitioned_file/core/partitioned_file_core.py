from file_with_size import FileWithSize


class PartitionedFileCore(object):
    def __init__(self, file_path, partition_size=64 * 1024 * 1024):
        self._file_path = file_path
        self._partition_size = partition_size
        self._idx = 0
        self._file_object = None

    def write(self, payload):
        self._file_object.write(payload)
        self._file_object.flush()
        if self.is_greater_than_max_partition_size:
            self.close()
            self._idx += 1
            self.__enter__()

    @property
    def is_greater_than_max_partition_size(self):
        print self.file_object.size
        return self.file_object.size > self._partition_size

    @property
    def file_name(self):
        return self._file_path.replace('*', str(self._idx))

    @property
    def file_object(self):
        return self._file_object

    @classmethod
    def open(cls, *args, **kwargs):
        raise NotImplemented("PartitionedFileCore is an interface!")

    def set_file_handle(self, file_obj):
        self._file_object = FileWithSize(file_obj)

    def __enter__(self):
        raise NotImplemented("PartitionedFileCore is an interface!")

    def close(self):
        self.__exit__()

    def __exit__(self, *args, **kwargs):
        self._file_object.close()

