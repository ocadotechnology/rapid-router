#!/bin/bash
# To be used to docker deployment environment
export DEPLOYMENT=1
./manage.py collectstatic --noinput
./manage.py compress -f
./manage.py migrate
# flush memcache
echo "from django.core.cache import cache; cache.clear()" | ./manage.py shell
appcfg.py update --authenticate_service_account $DEPLOYMENT_CONFIG
