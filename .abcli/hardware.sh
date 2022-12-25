#! /usr/bin/env bash

function blue_sbc_hardware() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ] ; then
        abcli_show_usage "blue_sbc Hardware input" \
            "read Hardware inputs."
        abcli_show_usage "blue_sbc Hardware output <10101010>" \
            "activate hardware outputs to 10101010."
        abcli_show_usage "blue_sbc hardware validate" \
            "validate hardware."


        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.hardware --help
        fi
        return
    fi

    if [ "$task" == "input" ] ; then
        python3 -m blue_sbc.hardware \
            input \
            ${@:2}
        return
    fi

    if [ "$task" == "output" ] ; then
        python3 -m blue_sbc.hardware \
            output \
            --outputs "$2" \
            ${@:3}
        return
    fi

    if [ "$task" == "validate" ] ; then
        python3 -m blue_sbc.hardware \
            validate \
            ${@:2}
        return
    fi

    abcli_log_error "-blue_sbc: hardware: $task: command not found."
}
