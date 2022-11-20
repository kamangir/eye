#! /usr/bin/env bash

function abcli_install_grove() {
    pushd $abcli_path_git > /dev/null

    # https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi/
    curl -L https://github.com/Seeed-Studio/grove.py/raw/master/install.sh \
        --output grove_install.sh
    sudo bash ./grove_install.sh

    git clone https://github.com/kamangir/grove.py
    cd grove.py
    sudo pip3 install -e .

    # https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins/installation
    # sudo apt-get --yes --force-yes install avrdude

    # https://wiki.seeedstudio.com/Grove-Chainable_RGB_LED/
    # cd ..
    # git clone https://github.com/DexterInd/GrovePi.git
    # cd GrovePi/Firmware
    # sudo ./firmware_update.sh

    popd > /dev/null
}

if [ "$(abcli cookie read hat.type else)" == "grove" ] ; then
    abcli_install_module grove 106
fi