#! /usr/bin/env bash

abcli_source_caller_suffix_path /tests

abcli_env_dot_load \
    caller,filename=config.env,suffix=/..

abcli_env_dot_load \
    caller,ssm,plugin=blue_sbc,suffix=/../..

[[ "$abcli_is_github_workflow" == true ]] &&
    export BLUE_SBC_SESSION_IMAGER_ENABLED=0
