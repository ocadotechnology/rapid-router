#!/bin/bash
PROJECT_PATH=`pwd`
VIRTUALENV_NAME='ocargo'

# go up one directory to create a test envrionment :)
if [ -d ".git" ];
then
    echo 'Going up one directory'
    cd ..
fi
WORKSPACE=`pwd`


echo 'Creating dev-requirements.txt'
echo "-e git+https://github.com/ocadotechnology/django-nuit.git@0.7.0#egg=django-nuit
pyyaml==3.11
django-debug-toolbar==1.2.1" > $PROJECT_PATH/dev-requirements.txt

# install cloud sdk
echo 'Installing Google Cloud SDK'
echo $PATH | grep -q google-cloud-sdk > /dev/null 2>&1
if [ $? -ne 0 ];
then 
    curl https://sdk.cloud.google.com | bash
    source ~/.bashrc
    gcloud auth login
fi
# install virtualenv
echo 'Installing virtualenvwrapper'
pip freeze | grep virtualenvwrapper > /dev/null 2>&1
if [ $? -ne 0 ];
then
    pip install virtualenvwrapper
fi
# create virtualenv
source /opt/boxen/homebrew/bin/virtualenvwrapper.sh
cd $PROJECT_PATH
# check virtualenv exists
echo "Creating virtualenv called ${VIRTUALENV_NAME} - to use do 'workon ${VIRTUALENV_NAME}'"
lsvirtualenv | grep $VIRTUALENV_NAME > /dev/null 2>&1
if [ $? -ne 0 ];
then
    mkvirtualenv -a $PROJECT_PATH -i gitversion -i PIL $VIRTUALENV_NAME
fi
workon $VIRTUALENV_NAME
# dev requirements.txt
echo 'Installing dependencies from dev-requirements.txt'
pip freeze | grep ocargo > /dev/null 2>&1
if [ $? -ne 0 ];
then
    pip install -r ./dev-requirements.txt
fi

# (be able to switch to and from prod reqirements.txt)
echo 'Installing sass'
gem list | grep sass > /dev/null 2>&1
if [ $? -ne 0 ];
then
    sudo gem install sass --version '3.3.4'
fi

echo 'Doing local setup (syncdb, collectstatic)'
# create the database
./manage.py syncdb
# collectstatic
./manage.py collectstatic -l --noinput > /dev/null 2>&1
# compress
# ./manage.py compress
# echo starting command
echo "run 'workon ${VIRTUALENV_NAME}' to activate your virtualenv"
echo 'then run "./manage.py runserver" to run a local runserver'
echo 'then you can navigate to http://localhost:8000'


