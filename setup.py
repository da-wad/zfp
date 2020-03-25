from setuptools import setup, Extension, Command
import numpy as np

setup(
    name="zfpy-equinor",
    version="0.5.5",
    author="Peter Lindstrom",
    author_email="zfp@llnl.gov",
    description="zfp compression in Python",
    long_description="zfp compression in Python",
    ext_modules = [Extension('zfpy-equinor', ['build/python/zfpy.c'], 
                             include_dirs=['include', np.get_include()], 
                             libraries=['zfp'], library_dirs=['build/lib64'])]
)
