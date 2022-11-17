#! /usr/bin/env bash

function abcli_install_grove() {
    abcli_log "Installing..."
}

if [ "$(abcli cookie read session.screen display)" == "grove" ] ; then
    abcli_install_module grove 101
fi