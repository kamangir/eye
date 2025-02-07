# 🌀 blue-sbc

🌀 `@sbc` is an [`abcli`](https://github.com/kamangir/awesome-bash-cli) plugin for edge computing on [single board computers](https://github.com/kamangir/blue-bracket). 

```bash
pip install blue_sbc

# @env dot list
@env dot cp <env-name> local
```

--table--

```mermaid
graph LR
    camera["@sbc <camera> capture|preview image|video"]

    hardware_validate["@sbc <hardware> validate <options>"]

    session_start["@sbc session start"]

    object["📂 object"]:::folder
    camera_hardware["👁️‍🗨️ camera"]:::folder
    hardware["🖱️ hardware"]:::folder
    UI["💻 UI"]:::folder

    camera_hardware --> camera
    camera --> object
    camera --> UI

    hardware --> hardware_validate
    hardware_validate --> hardware
    hardware_validate --> UI

    hardware --> session_start
    session_start --> hardware
    camera_hardware --> session_start
    session_start --> object
    session_start --> UI

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

# branches

- [current](.) active and default branch.
- [main](https://github.com/kamangir/blue-sbc/tree/main) legacy branch, is running on [a cluster of Raspberry pis](https://github.com/kamangir/blue-bracket). ⚠️ do not touch. ⚠️

---

--signature--

