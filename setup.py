from setuptools import setup, find_packages

NAME = "nexus-api-python-client"
VERSION = "1.0.2"

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Nexus Repository Manager Python API Client",
    author="Simone Bruzzechesse",
    author_email="b.sim619@gmail.com",
    url="",
    keywords=["Nexus API", "Python", "Nexus Repository Manager REST API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Sonatype Nexus API Client for Python (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
    """
)
