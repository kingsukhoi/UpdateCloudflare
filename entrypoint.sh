#!/usr/bin/env sh

main(){
    #SECRETS_LOC
    if [ -f $SECRETS_LOC ]; then
        (>&2 echo "file not found")
        exit 1
    fi

    watch -n 1200 python /opt/workdir/driver.py "$SECRETS_LOC"
}

main
