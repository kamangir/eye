#! /usr/bin/env bash

function blue_sbc_camera() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        abcli_show_usage "blue_sbc camera capture image" \
            "capture an image from camera."
        abcli_show_usage "blue_sbc camera capture video [--length 10] [--preview 1]" \
            "[preview and] capture [10 s] of video."
        abcli_show_usage "blue_sbc camera preview" \
            "preview camera."

        return
    fi

    if [[ "|capture|preview|" == *"|$task|"* ]]; then
        local options=$2
        local capture_video=$(abcli_option_int "$options" video 0)
        [[ "$capture_video" == 1 ]] &&
            task=capture_video

        python3 -m blue_sbc.imager.camera \
            $task \
            "${@:3}"

        return
    fi

    python3 -m blue_sbc.imager.camera "$@"
}
