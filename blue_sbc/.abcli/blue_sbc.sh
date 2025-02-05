#! /usr/bin/env bash

function bsbc() {
    blue_sbc $@
}

function blue_sbc() {
    local task=$(abcli_unpack_keyword $1 version)

    if [ $task == "help" ]; then
        blue_sbc_adafruit_rgb_matrix $@
        blue_sbc_camera $@
        blue_sbc_grove $@
        blue_sbc_hat $@
        blue_sbc_lepton $@
        blue_sbc_scroll_phat_hd $@
        blue_sbc_session $@
        blue_sbc_sparkfun_top_phat $@
        blue_sbc_unicorn_16x16 $@
        return
    fi

    local function_name=blue_sbc_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name ${@:2}
        return
    fi

    python3 -m blue_sbc "$@"
}

abcli_log $(blue_sbc version --show_icon 1)
