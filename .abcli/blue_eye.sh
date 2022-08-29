#! /usr/bin/env bash

function bsbc() {
    blue_sbc $@
}

function blue_sbc() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        blue_sbc_camera $@
        blue_sbc_session $@
        return
    fi

    if [[ $(type -t blue_sbc_$task) == "function" ]] ; then
        blue_sbc_$task ${@:2}
        return
    fi

    abcli_log_error "-blue_sbc: $task: command not found."
}