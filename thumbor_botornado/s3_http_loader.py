from botornado.s3.bucket import AsyncBucket
from botornado.s3.connection import AsyncS3Connection
from botornado.s3.key import AsyncKey

from thumbor_botornado.s3_loader import S3Loader
from thumbor.loaders.http_loader import HttpLoader

def load(context, url, callback):
	p = re.compile('/^https?:/i')
	m = p.match(url)
	if m:
		HttpLoader.load(context, url, callback)
	else:
		S3Loader.load(context, url, callback)
