from setuptools import setup, find_packages

setup(
    name = 'thumbor_botornado',
    version = "2.0.0",
    description = 'Thumbor S3 integration via botornado',
    author = 'Paul Annesley',
    author_email = 'paul@99designs.com',
    zip_safe = False,
    include_package_data = True,
    packages=find_packages(),
    install_requires=[
        'thumbor>=5.0.0',
        'botornado==0.0.3',
    ]
)
