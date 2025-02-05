from blueness.pypi import setup

from blue_sbc import NAME, VERSION, DESCRIPTION, REPO_NAME

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.algo",
        f"{NAME}.applications",
        f"{NAME}.hardware",
        f"{NAME}.hardware.hat",
        f"{NAME}.hardware.sparkfun_top_phat",
        f"{NAME}.imager",
        f"{NAME}.imager.camera",
        f"{NAME}.imager.lepton",
        f"{NAME}.session",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
        ],
    },
)
