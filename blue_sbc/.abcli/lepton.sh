#! /usr/bin/env bash

function blue_sbc_lepton() {
    local task=$(abcli_unpack_keyword $1 version)

    if [[ "|capture|preview|" == *"|$task|"* ]]; then
        python3 -m blue_sbc.imager.lepton \
            $task \
            --output_path $abcli_object_path \
            "${@:2}"
        return
    fi

    python3 -m blue_sbc.imager.lepton "$@"
}
