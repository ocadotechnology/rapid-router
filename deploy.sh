#!/bin/bash
# To be used to docker deployment environment
export DEPLOYMENT=1
./manage.py collectstatic --noinput
./manage.py compress -f
./manage.py flush --noinput
./manage.py syncdb --noinput
appcfg.py update --authenticate_service_account $1
