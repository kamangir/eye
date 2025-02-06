#! /usr/bin/env bash

function blue_sbc_session() {
    local task=$(abcli_unpack_keyword $1 start)

    if [ "$task" == "start" ]; then
        local options=$2
        local do_dryrun=$(abcli_option_int "$options" dryrun 0)
        local app_name=$(abcli_option "$options" app $BLUE_SBC_APPLICATION)
        local run_sudo=$(abcli_option_int "$options" sudo 0)
        local do_upload=$(abcli_option_int "$options" upload 1)

        local object_name=blue_sbc_session-$(abcli_string_timestamp_short)

        abcli_log "@sbc: session started $options $app_name -> $object_name"

        abcli_mlflow_tags_set \
            $object_name \
            session,host=$abcli_hostname,$BLUE_SBC_SESSION_OBJECT_TAGS,app=$app_name

        local extra_args=""
        [[ ! -z "$app_name" ]] &&
            extra_args="--application $app_name"

        local sudo_prefix=""
        # https://stackoverflow.com/a/8633575/17619982
        [[ "$run_sudo" == 1 ]] &&
            sudo_prefix="sudo -E "

        abcli_eval dryrun=$do_dryrun \
            $sudo_prefix \
            python3 -m blue_sbc.session \
            start \
            --object_name $object_name \
            $extra_args \
            "${@:3}"
        local status="$?"

        [[ "$do_upload" == 1 ]] &&
            abcli_upload - $object_name

        abcli_log "@sbc: session ended."

        return $status
    fi

    python3 -m blue_sbc.session "$@"
}
