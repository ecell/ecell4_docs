#!/bin/bash -ex

USER_ID=${LOCAL_UID:-9001}
GROUP_ID=${LOCAL_GID:-9001}
useradd -u $USER_ID -o -m user
groupmod -g $GROUP_ID user
chown -hR user:user /root
chown -hR user:user /opt
exec /usr/sbin/gosu user bash -e < ./main.sh
