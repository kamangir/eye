#! /usr/bin/env bash

function be() {
    blue_eye $@
}

function blue_eye() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        blue_eye_session $@
        return
    fi

    if [[ $(type -t blue_eye_$task) == "function" ]] ; then
        blue_eye_$task ${@:2}
        return
    fi

    abcli_log_error "-blue_eye: $task: command not found."
}