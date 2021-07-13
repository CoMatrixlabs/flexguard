import os
import io
from setuptools import setup, find_packages


# Helpers


def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding="utf-8").read().strip()
    return contents


# Prepare


PACKAGE = "frictionless"
NAME = PACKAGE.replace("_", "-")
TESTS_REQUIRE = [
    "mypy",
    "moto",
    "black",
    "jinja2",
    "pylama",
    "pytest",
    "ipython",
    "pymysql",
    "goodread",
    "psycopg2",
    "pytest-cov",
    "pytest-vcr",
    "pytest-only",
    "oauth2client",
    "requests-mock",
    "python-dotenv",
    "pydoc-markdown",
    "docstring-parser",
]
EXTRAS_REQUIRE = {
    "bigquery": ["google-api-python-client>=1.12.1"],
    "ckan": ["ckanapi>=4.3"],
    "excel": ["openpyxl>=3.0", "xlrd>=1.2", "xlwt>=1.2"],
    "gsheets": ["pygsheets>=2.0"],
    "html": ["pyquery>=1.4"],
    "json": ["ijson>=3.0", "jsonlines>=1.2"],
    "ods": ["ezodf>=0.3", "lxml>=4.0"],
    "pandas": ["pandas>=1.0"],
    "s3": ["boto3>=1.9"],
    "server": ["gunicorn>=20.0", "flask>=1.1"],
    "spss": ["savReaderWriter>=3.0"],
    "sql": ["sqlalchemy>=1.3"],
    "dev": TESTS_REQUIRE,
}
INSTALL_REQUIRES = [
    "petl>=1.6",
    "pyyaml>=5.3",
    "isodate>=0.6",
    "rfc3986>=1.4",
    "chardet>=3.0",
    "requests>=2.10",
    "jsonschema>=2.5",
    "simpleeval>=0.9",
    "stringcase>=1.2",
    "typer[all]>=0.3",
    "validators>=0.18",
    "python-slugify>=1.2",
    "python-dateutil>=2.8",
    "amundsen-databuilder>=4.2.0",
    "numpy>=1.19.3",
    "oauthlib==3.1.0",
    "opendp-smartnoise>=0.1.3.1",
    "opendp-smartnoise-core>=0.2.2",
    "PyYAML>=5.4.1",
    "scikit-learn==0.24.2",
    "scikit-learn-extra==0.1.0b2",
    "scipy==1.7.0"
]
README = read("README.md")
VERSION = read(PACKAGE, "assets", "VERSION")
PACKAGES = find_packages(exclude=["tests"])
ENTRY_POINTS = {"console_scripts": ["cryptopackage = cryptopackage.__main__:program"]}


# Run


setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require=EXTRAS_REQUIRE,
    entry_points=ENTRY_POINTS,
    zip_safe=False,
    long_description=README,
    long_description_content_type="text/markdown",
    description="Cryptopackage is a framework for data curation and governance",
    author="CoMatrix",
    author_email="support@comatrixlabs.io",
    url="https://github.com/comatrix/flexguard",
    license="MIT",
    keywords=[
        "data validation",
        "privacy policies",
        "json schema",
        "json table schema",
        "data package"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
