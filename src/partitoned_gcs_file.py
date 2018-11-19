import json
import uuid
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
        return self


class PartitionedGCSGzipFile(PartitionedGCSFileCore):
    def __init__(self, project_id, bucket, file_path, partition_size=64 * 1024 * 1024):
        super(PartitionedGCSGzipFile, self).__init__(project_id, bucket, file_path, partition_size)

    def __enter__(self):
        gcs_filesystem = gcsfs.GCSFileSystem(project=self.project_id)
        h1 = gcs_filesystem.open(self.gcs_full_path, 'wb')
        h = GzipFile(fileobj=h1, mode='wb')
        self.set_file_handle(h)
        return self


if __name__ == '__main__':

    pl = dict(
        name="a",
        id=1,
        value=100.5,
        text="random text",
        uuid=str(uuid.uuid4()),
        _2=range(1, 10),
        text2="random text2"
    )

    pl_text = json.dumps(pl)
    with PartitionedGCSGzipFile('just-data-sandbox', 'just-data-airflow-integration-test-dev', "test/test_*.json.gz", partition_size=1024 * 1024) as pf:
        for i in range(1, 20000):
            pf.write(pl_text+'\n'+pl_text+'\n'+pl_text+'\n'+pl_text+'\n')