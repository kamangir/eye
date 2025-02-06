# 🌀 blue-sbc

🌀 `@sbc` is an [`abcli`](https://github.com/kamangir/awesome-bash-cli) plugin for edge computing on [single board computers](https://github.com/kamangir/blue-bracket). 

```bash
pip install blue_sbc
```

--table--

```mermaid
graph LR

    lepton_capture["@sbc lepton capture"]
    lepton_preview["@sbc lepton preview"]

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

--signature--