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
    install_requires=['thumbor','botornado']
)
