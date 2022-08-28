#! /usr/bin/env bash

function blue_eye_camera() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_eye camera capture [image|video]" \
            "capture an image|video."
        abcli_help_line "blue_eye camera preview" \
            "preview camera."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_eye.camera --help
        fi

        return
    fi

    if [ "$task" == "capture" ] ; then
        return
    fi

    if [ "$task" == "preview" ] ; then
        return
    fi

    abcli_log_error "-blue-eye: camera: $task: command not found."
}