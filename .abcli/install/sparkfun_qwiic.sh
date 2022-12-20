#! /usr/bin/env bash

function abcli_install_sparkfun_qwiic() {
    # https://learn.sparkfun.com/tutorials/sparkfun-top-phat-hookup-guide/button-controller
    sudo pip3 install sparkfun-qwiic

    # https://learn.sparkfun.com/tutorials/sparkfun-top-phat-hookup-guide/ws2812b-leds
    sudo pip3 install adafruit-circuitpython-neopixel

    pushd $abcli_path_home/git > /dev/null
    git clone https://github.com/sparkfun/Top_pHAT_Button_Py
    popd > /dev/null
}

if [ "$(abcli cookie read hat.kind else)" == "sparkfun-top-phat" ] ; then
    abcli_install_module sparkfun_qwiic 101
fi