#!/bin/bash
# To be used to docker deployment environment
cd /opt/ocargo
export DEPLOYMENT=1
./manage.py flush --noinput
./manage.py syncdb --noinput
./manage.py collectstatic --noinput
./manage.py compress -f
appcfg.py update --oauth2 --noauth_local_webserver .
