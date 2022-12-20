#! /usr/bin/env bash

function blue_sbc_sparkfun_qwiic() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "blue_sbc sparkfun_qwiic validate" \
            "validate sparkfun_qwiic."
        return
    fi

    if [ "$task" == "validate" ] ; then
        pushd $abcli_path_git/Top_pHAT_Button_Py/examples > /dev/null
        python3 top_phat_button_ex2.py
        popd > /dev/null
        return
    fi

    abcli_log_error "-blue-sbc: sparkfun_qwiic: $task: command not found."
}