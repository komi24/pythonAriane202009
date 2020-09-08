# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
      name="say_hello",
      description=" Library for saying hello",
      version="1.0.0",
      packages=["MonPackage"],
      package_dir={"MonPackage": "src/MonPackage"}
)