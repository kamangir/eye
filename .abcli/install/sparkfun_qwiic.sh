#! /usr/bin/env bash

function abcli_install_sparkfun_qwiic() {
    # https://learn.sparkfun.com/tutorials/sparkfun-top-phat-hookup-guide/button-controller
    sudo pip3 install sparkfun-qwiic
}

if [ "$(abcli cookie read hat.kind else)" == "sparkfun-top-phat" ] ; then
    abcli_install_module sparkfun_qwiic 101
fi