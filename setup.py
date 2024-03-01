#!/usr/bin/env python
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

d = generate_distutils_setup()

d["packages"] = ["cv_bridge_customize"]
d["package_dir"] = {"": "python"}

setup(**d)
