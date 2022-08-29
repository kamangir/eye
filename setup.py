from setuptools import setup

from blue_sbc import NAME, VERSION

setup(
    name=NAME,
    author="kamangir",
    version=VERSION,
    description="an abcli plugin for cloud-connected raspberry pi/jetson hardware",
    packages=[NAME],
)
