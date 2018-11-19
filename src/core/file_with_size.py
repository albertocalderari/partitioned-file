class FileWithSize(object):
    def __init__(self, file_handle):
        self._file_handle = file_handle
        self._written_bytes = 0

    @property
    def written_bytes(self):
        return self._written_bytes

    def write(self, payload):
        self._file_handle.write(payload)
        self.increment_written_bytes(payload)

    @staticmethod
    def n_bytes(payload):
        return len(payload.encode('utf8'))

    def increment_written_bytes(self, payload):
        self._written_bytes += self.n_bytes(payload)

    def close(self):
        self._file_handle.close()

    def flush(self):
        self._file_handle.flush()