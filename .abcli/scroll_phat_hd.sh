#! /usr/bin/env bash

function blue_sbc_scroll_phat_hd() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_help_line "blue_sbc scroll_phat_hd validate" \
            "validate scroll_phat_hd."
        return
    fi

    if [ "$task" == "validate" ] ; then
        pushd $bolt_path_git/scroll-phat-hd//examples > /dev/null
        python3 plasma.py
        popd > /dev/null
    fi

    abcli_log_error "-blue-sbc: scroll_phat_hd: $task: command not found."
}