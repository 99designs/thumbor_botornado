from setuptools import setup, find_packages

setup(
    name = 'thumbor_botornado',
    version = "0.1",
    description = 'Thumbor S3 integration via botornado',
    author = 'Paul Annesley',
    author_email = 'paul@99designs.com',
    zip_safe = False,
    include_package_data = True,
    packages=find_packages(),
    install_requires=[
        'thumbor>=4.0.0,<5.0.0',
        'tornado>2.3.0,<4.0.0',
        'botornado==0.0.3',
    ]
)
