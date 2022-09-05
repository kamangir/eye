#! /usr/bin/env bash

function blue_sbc_lepton() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_sbc lepton capture image" \
            "capture an image from lepton."
        abcli_help_line "blue_sbc lepton preview" \
            "preview lepton."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.imager.lepton --help
        fi

        return
    fi

    if [ "$task" == "capture" ] ; then
        python3 -m blue_sbc.imager.lepton \
            capture \
            --output_path $abcli_object_path\ \
            ${@:2}
        return
    fi

    if [ "$task" == "preview" ] ; then
        python3 -m blue_sbc.imager.lepton \
            preview \
            ${@:2}
        return
    fi

    abcli_log_error "-blue-sbc: lepton: $task: command not found."
}