#! /usr/bin/env bash

function blue_sbc_session() {
    local task=$(abcli_unpack_keyword $1 start)

    if [ "$task" == "start" ]; then
        local options=$2
        local do_dryrun=$(abcli_option_int "$options" dryrun 0)
        local app_name=$(abcli_option "$options" app $BLUE_SBC_APPLICATION)
        local run_sudo=$(abcli_option_int "$options" sudo 0)
        local do_upload=$(abcli_option_int "$options" upload 1)

        abcli_log "@sbc: session started $options $app_name"

        abcli_mlflow_tags_set \
            $abcli_object_name \
            open,session,$abcli_hostname,$(abcli_string_today),$BLUE_SBC_SESSION_OBJECT_TAGS,$app_name

        local extra_args=""
        [[ ! -z "$app_name" ]] &&
            extra_args="--application $app_name"

        local sudo_prefix=""
        # https://stackoverflow.com/a/8633575/17619982
        [[ "$run_sudo" == 1 ]] &&
            sudo_prefix="sudo -E "

        abcli_log dryrun=$do_dryrun \
            $sudo_prefix \
            python3 -m blue_sbc.session \
            start \
            $extra_args \
            "${@:3}"
        local status="$?"

        [[ "$do_upload" == 1 ]] &&
            abcli_upload - $abcli_object_name

        abcli_log "@sbc: session ended."

        return $status
    fi

    python3 -m blue_sbc.session "$@"
}
