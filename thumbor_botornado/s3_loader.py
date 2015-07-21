from botornado.s3.bucket import AsyncBucket
from botornado.s3.connection import AsyncS3Connection
from botornado.s3.key import AsyncKey
from tornado.concurrent import return_future

@return_future
def load(context, url, callback):
    bucket_name, object_name = url.split("/", 1)
    connection = AsyncS3Connection() # load credentials from environment
    bucket = AsyncBucket(connection, bucket_name)
    key = AsyncKey(bucket, object_name)
    key.read(callback=callback)
