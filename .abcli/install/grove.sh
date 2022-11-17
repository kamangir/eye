#! /usr/bin/env bash

function abcli_install_grove() {
    pushd $abcli_path_git > /dev/null
    # https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi/
    curl https://github.com/Seeed-Studio/grove.py/raw/master/install.sh \
        --output grove_install.sh
    #  | sudo bash -s -

    popd > /dev/null
}

if [ "$(abcli cookie read hat.type else)" == "grove" ] ; then
    abcli_install_module grove 103
fi