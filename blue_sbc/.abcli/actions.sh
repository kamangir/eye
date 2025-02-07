#! /usr/bin/env bash

function blue_sbc_action_git_before_push() {
    blue_sbc build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "current" ]] &&
        return 0

    blue_sbc pypi build
}
