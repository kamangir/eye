#! /usr/bin/env bash

function blue_sbc_golpy() {
    local task=$(abcli_unpack_keyword $1)

    if [ "$task" == "help" ] ; then
        abcli_help_line "blue_sbc golpy" \
            "simulate golpy"

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.algo.golpy --help
        fi
        return
    fi

    abcli_log "blue_sbc: algo: golpy: started..."

    python3 -m blue_sbc.algo.golpy \
        simulate \
        ${@:2}
}