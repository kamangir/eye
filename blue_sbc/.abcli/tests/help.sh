#! /usr/bin/env bash

function test_blue_sbc_help() {
    local options=$1

    local module
    for module in \
        "@sbc" \
        \
        "@sbc pypi" \
        "@sbc pypi browse" \
        "@sbc pypi build" \
        "@sbc pypi install" \
        \
        "@sbc pytest" \
        \
        "@sbc test" \
        "@sbc test list" \
        \
        "@sbc browse" \
        \
        "@sbc camera" \
        "@sbc camera capture" \
        "@sbc camera capture image" \
        "@sbc camera capture video" \
        "@sbc camera preview" \
        \
        "@sbc lepton" \
        "@sbc lepton capture" \
        "@sbc lepton preview" \
        \
        "@sbc scroll_phat_hd" \
        "@sbc scroll_phat_hd validate" \
        \
        "@sbc sparkfun_top_phat" \
        "@sbc sparkfun_top_phat validate" \
        \
        "blue_sbc"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
