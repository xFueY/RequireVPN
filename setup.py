from setuptools import setup, find_packages

Classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "License :: OSI Approved :: MIT License",
  "Natural Language :: English",
  "Programming Language :: Python :: 3.8"
]

setup(
  name="RequireVPN",
  version="0.0.2",
  description="Python Library To Require VPN Connections",
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url="https://github.com/xFueY/RequireVPN/",
  author="xFueY",
  author_email="xFueY@protonmail.com",
  license="MIT",
  classifiers=Classifiers,
  packages=find_packages(),
  keywords="RequireVPN",
  install_requires=["requests"]
)
