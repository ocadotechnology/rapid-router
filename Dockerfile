FROM python:2.7.14-stretch


# install python 2.7
RUN apt-get update -yqq \
  && apt-get install -yqq ruby python-pip \
  && rm -rf /var/lib/apt/lists
    
# install saas
RUN gem install sass -v 3.3.4

WORKDIR /usr/src/app

EXPOSE 8000
