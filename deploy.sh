#!/bin/bash
# To be used to docker deployment environment
export DEPLOYMENT=1
./manage.py collectstatic --noinput
./manage.py compress -f
./manage.py sqlclear auth | ./manage.py dbshell
./manage.py sqlclear game | ./manage.py dbshell
./manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'coding-for-life-xd@ocado.com', '$ADMIN_PASSWORD')" | ./manage.py shell
# flush memcache
echo "from django.core.cache import cache; cache.clear()" | ./manage.py shell
appcfg.py update --authenticate_service_account $DEPLOYMENT_CONFIG
