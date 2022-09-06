#! /usr/bin/env bash

function abcli_install_scroll_phat_hd() {
    echo "wip"
}

if [ "$(abcli cookie read session.screen display)" == "scroll_phat_hd" ] ; then
    abcli_install_module scroll_phat_hd 102
fi