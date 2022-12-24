#! /usr/bin/env bash

function abcli_install_blue_sbc_template() {
    abcli_log "wip"
}

if [ "$(abcli cookie read hardware.kind other)" == "blue_sbc_template" ] ; then
    abcli_install_module blue_sbc_template 101
fi