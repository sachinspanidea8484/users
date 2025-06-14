#!/usr/bin/env python
import os
import sys

from setuptools import find_packages, setup

from openwisp_users import get_version


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open("requirements.txt").readlines():
        # skip to next iteration if comment or empty line
        if (
            line.startswith("#")
            or line == ""
            or line.startswith("http")
            or line.startswith("git")
        ):
            continue
        # add line to requirements
        requirements.append(line)
    return requirements


if sys.argv[-1] == "publish":
    # delete any *.pyc, *.pyo and __pycache__
    os.system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload -s dist/*")
    os.system("rm -rf dist build")
    args = {"version": get_version()}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name="openwisp-users",
    #version=get_version(),
    version="1.2.0a0",
    license="BSD",
    author="OpenWISP",
    author_email="support@openwisp.io",
    description="Provides basic multi-tenancy features for OpenWISP (using the Django web-framework)",
    long_description=open("README.rst").read(),
    url="http://openwisp.org",
    download_url="https://github.com/openwisp/openwisp-users/releases",
    platforms=["Platform Independent"],
    keywords=["openwisp", "django", "organizations", "users"],
    packages=find_packages(exclude=["tests*", "docs*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_install_requires(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Topic :: Internet :: WWW/HTTP",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
