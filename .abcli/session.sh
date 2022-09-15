#! /usr/bin/env bash

function blue_sbc_session() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_sbc session start [<options>]" \
            "start a blue_sbc session."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.session --help
        fi

        return
    fi

    if [ "$task" == "start" ] ; then
        abcli_log "blue-sbc: session started."

        abcli_tag set \
            $abcli_object_name \
            open,session,$abcli_hostname,$(abcli_string_today),$(abcli_cookie read session.object.tags)

        local options="$2"

        python3 -m blue_sbc.session \
            start \
            ${@:3}

        abcli_upload open

        abcli_log "blue-sbc: session ended."

        return
    fi

    abcli_log_error "-blue-sbc: session: $task: command not found."
}