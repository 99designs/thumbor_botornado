thumbor_botornado
=================

thumbor_botornado provides an S3 loader for [Thumbor] using the [botornado] async AWS S3 client.

Credentials are loaded from environment or filesystem as per [boto configuration][boto-config] - generally `$AWS_ACCESS_KEY_ID` and `$AWS_SECRET_ACCESS_KEY` or `~/.aws/credentials`.

There are no configuration parameters - access control should be enforced with Thumbor URL signing and AWS access key policies.

Implementation can be seen in [s3_loader.py](thumbor_botornado/s3_loader.py).

thumbor_botornado was inspired by [thumbor_aws] which has more configuration options, but at time of writing uses a blocking S3 client, limiting concurrency.


Usage
-----

Install:

```sh
pip install https://github.com/99designs/thumbor_botornado/archive/master.tar.gz
```

You should probably replace `master` with a stable tag or SHA1 from [the releases page](https://github.com/99designs/thumbor_botornado/releases).

In your `thumbor.conf`:

```python
LOADER = 'thumbor_botornado.s3_loader'
```

Ensure you have [boto-discoverable AWS credentials][boto-config].

Then just use `bucket-name/object-path` instead of a full URL in Thumbor URLs. To load `images/example.png` from an S3 bucket named `example-assets` without signature or filters etc, the Thumbor URL would be `http://thumbor-hostname.example/unsafe/example-assets/images/example.png`.


[Thumbor]: https://github.com/thumbor/thumbor
[botornado]: https://github.com/yyuu/botornado
[boto-config]: http://boto.readthedocs.org/en/latest/boto_config_tut.html
[thumbor_aws]: https://github.com/willtrking/thumbor_aws


License
-------

© 2014 99designs Inc. Released under the MIT license.
