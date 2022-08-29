#! /usr/bin/env bash

function blue_sbc_camera() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_sbc camera capture image" \
            "capture an image."
        abcli_help_line "blue_sbc camera capture video [--length 10] [--preview 1]" \
            "[preview and] capture [10 s] of video."
        abcli_help_line "blue_sbc camera preview" \
            "preview camera."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.camera --help
        fi

        return
    fi

    if [ "$task" == "capture" ] ; then
        local options=$2
        local capture_video=$(abcli_option_int "$options" "video" 0)

        if [ "$capture_video" == "1" ] ; then
            python3 -m blue_sbc.camera \
                capture_video \
                ${@:3}
        else
            python3 -m blue_sbc.camera \
                capture \
                --output_path $abcli_object_path\ \
                ${@:3}
        fi

        return
    fi

    if [ "$task" == "preview" ] ; then
        python3 -m blue_sbc.camera \
            preview \
            ${@:2}
        return
    fi

    abcli_log_error "-blue-sbc: camera: $task: command not found."
}