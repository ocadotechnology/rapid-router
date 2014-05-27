#!/bin/bash
# To be used to docker deployment environment
export DEPLOYMENT=1
./manage.py collectstatic --noinput
./manage.py compress -f
./manage.py sqlclear game | ./manage.py dbshell
./manage.py syncdb --noinput
appcfg.py update --authenticate_service_account $DEPLOYMENT_CONFIG
