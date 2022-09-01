# blue-sbc

`blue-sbc` is an [abcli](https://github.com/kamangir/awesome-bash-cli) plugin for [Raspberry Pi](#Raspberry-Pi)/[Jeson](#Jetson-Nano) cloud-connected hardware, including camera, that run deep learning vision models through python and TensorFlow ([more examples](https://github.com/kamangir/blue-bracket)).

| [![image](https://github.com/kamangir/blue-bracket/raw/main/images/cube-1.jpg)](#Raspberry-Pi) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/eye_nano-1.jpg)](#Jetson-Nano) | 
|---|---|

## Raspberry Pi

Build the hardware according to [cube](https://github.com/kamangir/blue-bracket/blob/main/designs/cube.md).

Type in,
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

## Jetson Nano

1. Build the hardware according to [eye-nano](https://github.com/kamangir/blue-bracket/blob/main/designs/eye_nano.md).
2. 🚧