# 🌀 blue-sbc

🌀 `@sbc` is an [`abcli`](https://github.com/kamangir/awesome-bash-cli) plugin for edge computing on [single board computers](https://github.com/kamangir/blue-bracket). 

```bash
pip install blue_sbc
```

--table--

```mermaid
graph LR

    lepton["@sbc lepton capture|preview"]

    camera["@sbc camera capture|preview image|video"]

    object["📂 object"]:::folder
    camera_hardware["👁️‍🗨️ camera"]:::folder
    UI["💻 UI"]:::folder

    camera_hardware --> lepton
    lepton --> object
    lepton --> UI

    camera_hardware --> camera
    camera --> object
    camera --> UI

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

---

--signature--