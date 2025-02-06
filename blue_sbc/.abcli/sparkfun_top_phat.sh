#! /usr/bin/env bash

function blue_sbc_sparkfun_top_phat() {
    local task=$(abcli_unpack_keyword $1 version)

    if [ "$task" == "validate" ]; then
        local what=$(abcli_clarify_input $2 button)

        if [ "$what" == button ]; then
            pushd $abcli_path_git/Top_pHAT_Button_Py/examples >/dev/null
            python3 top_phat_button_ex2.py
            popd >/dev/null
            return
        fi

        if [ "$what" == leds ]; then
            sudo python3 -m blue_sbc.hardware.sparkfun_top_phat \
                validate_leds
            return
        fi

        sudo python3 -m blue_sbc.hardware.sparkfun_top_phat "$@"
        return
    fi

    sudo python3 -m blue_sbc.hardware.sparkfun_top_phat "$@"
}
