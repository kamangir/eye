#! /usr/bin/env bash

function blue_sbc_session() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_sbc session start [output=screen]" \
            "start a blue_sbc session."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.session --help
        fi

        return
    fi

    if [ "$task" == "start" ] ; then
        abcli_log "blue-sbc: session started."

        abcli_tag set $abcli_object_name session,$abcli_host_name,$(abcli_string_today),$abcli_fullname,open,$abcli_wifi_ssid

        local options="$2"
        local output=""
        if [[ "$abcli_is_mac" == true ]] ; then
            local output="screen"
        elif [[ "$abcli_is_rpi" == true ]] && [[ "$abcli_is_headless" == false ]] ; then
            local output="screen"
        fi
        local output=$(abcli_option "$options" "output" $output)

        local extra_args=""
        if [ ! -z "$output" ] ; then
            local extra_args="--output $output"
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