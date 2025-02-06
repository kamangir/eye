#! /usr/bin/env bash

function blue_sbc_hat() {
    local task=$(abcli_unpack_keyword $1 help)

    if [[ "|input|validate|" == *"|$task|"* ]]; then
        python3 -m blue_sbc.hardware.hat \
            $task \
            "${@:2}"
        return
    fi

    if [ "$task" == "output" ]; then
        python3 -m blue_sbc.hardware.hat \
            output \
            --outputs "$2" \
            "${@:3}"
        return
    fi

    python3 -m blue_sbc.hardware.hat "$@"
}
