#! /usr/bin/env bash

function test_blue_sbc_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_sbc version ${@:2}"
}
