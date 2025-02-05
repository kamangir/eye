#! /usr/bin/env bash

function blue_sbc_sparkfun_top_phat() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "blue_sbc sparkfun_top_phat validate [button|leds]" \
            "validate sparkfun_top_phat."
        return
    fi

    if [ "$task" == "validate" ] ; then
        local what=$(abcli_clarify_input $2 button)

        if [ "$what" == button ] ; then
            pushd $abcli_path_git/Top_pHAT_Button_Py/examples > /dev/null
            python3 top_phat_button_ex2.py
            popd > /dev/null
            return
        fi

        if [ "$what" == leds ] ; then
            sudo python3 -m blue_sbc.hardware.sparkfun_top_phat \
                validate_leds
            return
        fi

        abcli_log_error "- blue-sbc: sparkfun_top_phat: $task: $what: hardware not found."
        return
    fi

    abcli_log_error "-blue-sbc: sparkfun_top_phat: $task: command not found."
}