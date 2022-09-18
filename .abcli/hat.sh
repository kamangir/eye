#! /usr/bin/env bash

function blue_sbc_hat() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ] ; then
        abcli_show_usage "blue_sbc hat input" \
            "read hat inputs."
        abcli_show_usage "blue_sbc hat output <10101010>" \
            "activate hat outputs to 10101010."
        abcli_show_usage "blue_sbc hat validate" \
            "validate hat."


        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.hat --help
        fi
        return
    fi

    if [ "$task" == "input" ] ; then
        python3 -m blue_sbc.hat \
            input \
            ${@:2}
        return
    fi

    if [ "$task" == "output" ] ; then
        python3 -m blue_sbc.hat \
            output \
            --outputs "$2" \
            ${@:3}
        return
    fi

    if [ "$task" == "validate" ] ; then
        python3 -m blue_sbc.hat \
            validate \
            ${@:2}
        return
    fi

    abcli_log_error "-blue_sbc: hat: $task: command not found."
}
