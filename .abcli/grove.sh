#! /usr/bin/env bash

function blue_sbc_grove() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "blue_sbc grove validate${ABCUL}[button]" \
            "validate grove."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.hat --help
        fi

        return
    fi

    if [ "$task" == "validate" ] ; then
        local what=$(abcli_clarify_input $2 button)
        abcli_log "validating grove $what..."

        if [ "$what" == "button" ]; then
            pushd $abcli_path_git/grove.py/grove > /dev/null
            python3 grove_button.py
            popd > /dev/null
            return
        fi

        abcli_log_error "-blue-sbc: grove: $task: $what: hardware not found."
        return
    fi

    abcli_log_error "-blue-sbc: grove: $task: command not found."
}