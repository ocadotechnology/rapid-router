FROM python:3.7-slim-stretch@sha256:fdded80ae770ada550d33964ea383696c44548f76cbf4b07c4b4743a8e4a1045


# install python 2.7
RUN apt-get update -yqq \
  && apt-get install -yqq ruby python-pip \
  && rm -rf /var/lib/apt/lists
    
# install saas
RUN gem install sass -v 3.3.4

WORKDIR /usr/src/app

EXPOSE 8000
