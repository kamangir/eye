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
        "@sbc leaf" \
        \
        "@sbc task" \
        \
        "blue_sbc"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
