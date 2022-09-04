# blue-sbc

`blue-sbc` is an [`abcli`](https://github.com/kamangir/awesome-bash-cli) plugin for Raspberry Pi/Jeson cloud-connected hardware, including camera, that run deep learning vision models through python and TensorFlow. Click on each design for more info on the hardware setup.

| [![image](https://github.com/kamangir/blue-bracket/raw/main/images/blue3-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/blue3.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/chenar-grove-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/chenar-grove.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/cube-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/cube.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/eye_nano-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/eye_nano.md) | 
|---|---|---|---|

To install `blue-sbc`, first install [`abci`](https://github.com/kamangir/awesome-bash-cli) on the machine, then open a terminal and type in,

```bash
abcli git clone blue-sbc install
abcli cookie cp mirror
abcli init
abcli session start
```