# blue-sbc

`blue-sbc` is an [abcli](https://github.com/kamangir/awesome-bash-cli) plugin for Raspberry Pi/Jeson cloud-connected hardware, including camera, that run deep learning vision models through python and TensorFlow. Click on each design for more info on the hardware setup.

| [![image](https://github.com/kamangir/blue-bracket/raw/main/images/blue3-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/blue3.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/chenar-grove-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/chenar-grove.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/cube-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/cube.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/eye_nano-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/eye_nano.md) | 
|---|---|

To install `blue-sbc` open a terminal on the machine and type in,
```bash
abcli git clone blue-sbc install
abcli cookie edit
```
and enter,
```json
{
    "session": "blue_sbc"
}
```

Optionally, you can also add,
```json
{
    "session.capture.enabled": false,
    "session.capture.period": 3000,
}
```

For additional control over the camera, display, hardware, and session add from below:
```json
{
    "camera.diff": 0.1,
    "camera.hi_res": true,
    "camera.rotation": 0,
    "camera": "lepton",
    "display.fullscreen": true,
    "hardware.hat": "led_switch",
    "messenger.recipients": "",
    "session.auto_upload": true,
    "session.display.period": 4,
    "session.messenger.period": 60,
    "session.outbound_queue": "stream",
    "session.reboot.period": 14400,
    "session.temperature.period": 300
}
```

To validate the install, type in:
```bash
abcli init
abcli session start
```