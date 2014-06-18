#!/bin/bash
# To be used to docker deployment environment
export DEPLOYMENT=1
./manage.py collectstatic --noinput
./manage.py compress -f
echo "** drop $DATABASE_NAME"
echo "drop database $DATABASE_NAME;" | ./manage.py dbshell
echo "** create $DATABASE_NAME"
echo "create database $DATABASE_NAME;" | ./manage.py dbshell
./manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'coding-for-life-xd@ocado.com', '$ADMIN_PASSWORD')" | ./manage.py shell
appcfg.py update --authenticate_service_account $DEPLOYMENT_CONFIG
