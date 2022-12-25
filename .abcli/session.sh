#! /usr/bin/env bash

function blue_sbc_session() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "blue_sbc session start$ABCUL[app=<application>]$ABCUL[<args>]" \
            "start a blue_sbc session."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.session --help
        fi

        return
    fi

    if [ "$task" == "start" ] ; then
        local options=$2
        local app_name=$(abcli_option "$options" app)

        abcli_log "blue-sbc: session started $options"

        abcli_tag set \
            $abcli_object_name \
            open,session,$abcli_hostname,$(abcli_string_today),$(abcli_cookie read session.object.tags),$app_name

        local extra_args=""
        if [ ! -z "$app_name" ] ; then
            local extra_args="--application $app_name"
        fi

        python3 -m blue_sbc.session \
            start \
            $extra_args \
            ${@:3}

        abcli_upload open

        abcli_log "blue-sbc: session ended."

        return
    fi

    abcli_log_error "-blue-sbc: session: $task: command not found."
}