#! /usr/bin/env bash

function blue_sbc_adafruit_rgb_matrix() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "blue_sbc adafruit_rgb_matrix validate" \
            "validate adafruit_rgb_matrix."
        return
    fi

    if [ "$task" == "validate" ] ; then
        pushd $abcli_path_git/Raspberry-Pi-Installer-Scripts/rpi-rgb-led-matrix/examples-api-use > /dev/null
        sudo ./demo -D0
        popd > /dev/null
        return
    fi

    abcli_log_error "-blue-sbc: adafruit_rgb_matrix: $task: command not found."
}