#!/usr/bin/env sh

main(){
    if [ $# -ne 1 ]; then
        (>&2 echo "file not found")
    fi

    file_loc="$1"

    watch -n 1200 python /opt/workdir/driver.py "${file_loc}"
}

main "$@"