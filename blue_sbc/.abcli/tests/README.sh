#! /usr/bin/env bash

function test_blue_sbc_README() {
    local options=$1

    abcli_eval ,$options \
        blue_sbc build_README
}
