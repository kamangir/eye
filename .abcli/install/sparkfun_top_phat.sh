#! /usr/bin/env bash

function abcli_install_sparkfun_top_phat() {
    # https://learn.sparkfun.com/tutorials/sparkfun-top-phat-hookup-guide/button-controller
    sudo pip3 install sparkfun-qwiic

    # https://learn.sparkfun.com/tutorials/sparkfun-top-phat-hookup-guide/ws2812b-leds
    sudo pip3 install adafruit-circuitpython-neopixel

    # https://github.com/rpi-ws281x/rpi-ws281x-python
    # https://github.com/jgarff/rpi_ws281x
    # https://stackoverflow.com/a/53045690/17619982
    sudo pip3 install rpi_ws281x

    pushd $abcli_path_home/git > /dev/null
    git clone https://github.com/sparkfun/Top_pHAT_Button_Py
    popd > /dev/null
}

if [ "$(abcli cookie read hardware.kind other)" == "sparkfun-top-phat" ] ; then
    abcli_install_module sparkfun_top_phat 104
fi