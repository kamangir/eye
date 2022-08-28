#! /usr/bin/env bash

function blue_eye_session() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_eye session start" \
            "start a blue_eye session."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_eye.session --help
        fi

        return
    fi

    if [ "$task" == "start" ] ; then
        abcli_log "blue-eye: session started."

        abcli_tag set $abcli_object_name session,$abcli_host_name,$(abcli_string_today),$abcli_fullname,open,$abcli_wifi_ssid

        python3 -m blue_eye.session start ${@:3}

        abcli_upload open

        abcli_log "blue-eye: session ended."
        return
    fi

    abcli_log_error "-blue-eye: session: $task: command not found."
}