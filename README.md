# 🌀 blue-sbc

🌀 `@sbc` is an [`abcli`](https://github.com/kamangir/awesome-bash-cli) plugin for edge computing on [single board computers](https://github.com/kamangir/blue-bracket). 

```bash
pip install blue_sbc
```

|   |   |   |   |
| --- | --- | --- | --- |
| [![image](https://github.com/kamangir/blue-bracket/raw/main/images/blue3-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/blue3.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/chenar-grove-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/chenar-grove.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/cube-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/cube.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/eye_nano-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/eye_nano.md) |

```mermaid
graph LR

    lepton_capture["@sbc<br>lepton<br>capture"]
    lepton_preview["@sbc<br>lepton<br>preview"]

    object["📂 object"]:::folder
    camera["👁️‍🗨️ camera"]:::folder
    UI["💻 UI"]:::folder

    camera --> lepton_capture
    lepton_capture --> object

    camera --> lepton_preview
    lepton_preview --> UI

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

---


[![pylint](https://github.com/kamangir/blue-sbc/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/blue-sbc/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/blue-sbc/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/blue-sbc/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/blue-sbc/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-sbc/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/blue-sbc.svg)](https://pypi.org/project/blue-sbc/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/blue-sbc)](https://pypistats.org/packages/blue-sbc)

built by 🌀 [`blue_options-4.210.1`](https://github.com/kamangir/awesome-bash-cli), based on 🌀 [`blue_sbc-7.20.1`](https://github.com/kamangir/blue-sbc).
