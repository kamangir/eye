#! /usr/bin/env bash

function grove() {
    blue_sbc_grove $@
}

function blue_sbc_grove() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "grove info" \
            "show grove info."
        abcli_show_usage "grove validate [adc|button]" \
            "validate grove adc | button."
        abcli_show_usage "grove validate oled_128x64$ABCUL[animate|buttons|image|shapes|stats]" \
            "validate grove oled_128x64."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m blue_sbc.hat --help
        fi

        return
    fi

    if [ "$task" == "info" ] ; then
        # https://learn.adafruit.com/scanning-i2c-addresses/raspberry-pi
        i2cdetect -y 1
        return
    fi

    if [ "$task" == "validate" ] ; then
        local what=$(abcli_clarify_input $2 button)

        local args=""
        local filepath="grove.py/grove"
        if [ "$what" == "adc" ]; then
            local filename="adc"
        elif [ "$what" == "button" ]; then
            local filename="grove_button"
            local args="24"
        elif [ "$what" == "oled_128x64" ]; then
            local filepath="Seeed_Python_SSD1315/examples"
            local filename="image"
        else
            abcli_log_error "- blue-sbc: grove: $task: $what: hardware not found."
            return
        fi

        local filename=$(abcli_clarify_input $3 $filename)

        local grove_path=$abcli_path_git/$filepath

        abcli_log "validating grove $what: $grove_path/$filename.py $args"
        pushd $grove_path > /dev/null
        python3 $filename.py $args
        popd > /dev/null

        return
    fi

    abcli_log_error "-blue-sbc: grove: $task: command not found."
}