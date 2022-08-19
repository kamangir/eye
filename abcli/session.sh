#! /usr/bin/env bash

function blue_eye_start_session() {
    abcli_log "blue-eye: session started."

    abcli_tag set $ABCLI_OBJECT_NAME session,$abcli_host_name,$(abcli_string_today),$abcli_fullname,open,$abcli_wifi_ssid

    python3 -m blue_eye start_session ${@:3}

    abcli_upload open

    abcli_log "blue-eye: session ended."
}