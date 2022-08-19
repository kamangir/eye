from setuptools import setup

from blue_eye import NAME, VERSION

setup(
    name=NAME,
    author="kamangir",
    version=VERSION,
    description="an abcli plugin for a cloud-connected raspberry pi/jetson camera",
    packages=[NAME],
)
