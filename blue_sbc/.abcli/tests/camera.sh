#! /usr/bin/env bash

function test_blue_sbc_camera_capture() {
    [[ "$BLUE_SBC_SESSION_IMAGER_ENABLED" == 0 ]] &&
        return 0

    local options=$1

    abcli_select \
        test_blue_sbc_camera_capture-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        blue_sbc_camera \
        capture \
        image
}

function test_blue_sbc_camera_capture_video() {
    [[ "$BLUE_SBC_SESSION_IMAGER_ENABLED" == 0 ]] ||
        [[ "$abcli_is_rpi" = false ]] &&
        return 0

    local options=$1

    abcli_select \
        test_blue_sbc_camera_capture_video-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        blue_sbc_camera \
        capture \
        video \
        --length 3 \
        --preview 1
}

function test_blue_sbc_camera_preview() {
    [[ "$BLUE_SBC_SESSION_IMAGER_ENABLED" == 0 ]] &&
        return 0

    local options=$1

    abcli_eval ,$options \
        blue_sbc_camera \
        preview \
        - \
        --length 3
}
