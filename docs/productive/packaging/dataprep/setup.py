import codecs
from setuptools import find_packages, setup
from Cython.Build import cythonize


with codecs.open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="dataprep",
    version="0.1.0",
    description="Toolbox for preparing data",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="http://github.com/veit/dataprep",
    author="Veit Schiele",
    author_email="veit@cusy.io",
    license="BSD-3-Clause",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["pandas"],
    ext_modules=cythonize("src/dataprep/cymean.pyx"),
)
