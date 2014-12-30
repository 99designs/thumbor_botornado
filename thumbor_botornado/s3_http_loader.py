import thumbor_botornado.s3_loader as S3Loader
import thumbor.loaders.http_loader as HttpLoader
import re

def load(context, url, callback):
	if re.match('https?:', url, re.IGNORECASE):
		HttpLoader.load(context, url, callback)
	else:
		S3Loader.load(context, url, callback)
