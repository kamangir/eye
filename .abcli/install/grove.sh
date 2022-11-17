#! /usr/bin/env bash

function abcli_install_grove() {
    abcli_log "Installing..."
}

if [ "$(abcli cookie read hat.type else)" == "grove" ] ; then
    abcli_install_module grove 102
fi