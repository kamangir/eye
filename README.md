# blue-sbc

`blue-sbc` is an [abcli](https://github.com/kamangir/awesome-bash-cli) plugin for [Raspberry Pi](#Raspberry-Pi)/[Jeson](#Jetson-Nano) cloud-connected hardware, including camera, that run deep learning vision models through python and TensorFlow ([more examples](https://github.com/kamangir/blue-bracket)).

| [![image](https://github.com/kamangir/blue-bracket/raw/main/images/cube-1.jpg)](#Raspberry-Pi) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/eye_nano-1.jpg)](#Jetson-Nano) | 
|---|---|

## Raspberry Pi

1. Build the hardware according to [cube](https://github.com/kamangir/blue-bracket/blob/main/designs/cube.md).
2. Type in,
```
abcli git clone blue-sbc
abcli init
abcli cookie edit
```
and enter,
```
{
    "session.capture.enabled": false,
    "session": "blue_sbc"
}
```
Ignore the first item if there is camera.
3. Type in to validate the install,
```
abcli session start
```

## Jetson Nano

1. Build the hardware according to [eye-nano](https://github.com/kamangir/blue-bracket/blob/main/designs/eye_nano.md).
2. 🚧