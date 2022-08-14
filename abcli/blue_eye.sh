#! /usr/bin/env bash

function eye() {
    blue_eye $@
}

function blue_eye() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_eye task_1" \
            "run blue_eye task_1."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_eye --help
        fi

        return
    fi

    if [ "$task" == "task_1" ] ; then
        python3 -m blue_eye \
            task_1 \
            ${@:2}
        return
    fi

    abcli_log_error "-blue_eye: $task: command not found."
}