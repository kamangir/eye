#! /usr/bin/env bash

function blue_sbc_golpy() {
    local task=$(abcli_unpack_keyword $1 simulate)

    if [ "$task" == "help" ] ; then
        abcli_show_usage "blue_sbc golpy simulate [--display 1]" \
            "simulate golpy [on display]."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.algo.golpy --help
        fi
        return
    fi

    if [ "$task" == "simulate" ] ; then
        abcli_log "blue_sbc: algo: golpy: started..."

        python3 -m blue_sbc.algo.golpy \
            simulate \
            ${@:2}

        return
    fi

    abcli_log_error "-blue_sbc: golpy: $task: command not found."
}