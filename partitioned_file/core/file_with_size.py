class FileWithSize(object):
    def __init__(self, file_obj):
        self._file_obj = file_obj

    @property
    def size(self):
        if hasattr(self._file_obj, 'fileobj'):
            # use the internal object when writing to a gzip file to get the correct size
            return self._file_obj.fileobj.tell()
        else:
            return self._file_obj.tell()

    def write(self, payload):
        self._file_obj.write(payload)

    def close(self):
        self._file_obj.close()

    def flush(self):
        self._file_obj.flush()