#!/usr/bin/env bash
! docker network create -d bridge jsonfield > /dev/null 2>&1
case "$(uname -s)" in

   Darwin)
    export DOCKER_IP="$(dinghy ip)"
     ;;

   Linux)
     export DOCKER_IP='localhost'
     ;;
   *)
     export DOCKER_IP='localhost'
     ;;
esac

if [[ $DOCKER_IP != "localhost" ]]; then
     dinghy ssh 'sudo ln -s /mnt/sda1 /data'
fi
export JSONFIELD_FOLDER=`pwd`
make start-dev
