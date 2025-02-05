#! /usr/bin/env bash

function blue_sbc() {
    local task=$(abcli_unpack_keyword $1 version)

    abcli_generic_task \
        plugin=blue_sbc,task=$task \
        "${@:2}"
}

abcli_log $(blue_sbc version --show_icon 1)
