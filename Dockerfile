# builds deployment environment and then push changes
FROM ubuntu:12.04
RUN apt-get update -qy
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client \
                                                      python-mysqldb \
                                                      python-dev \
                                                      python-pip \
                                                      build-essential \
                                                      curl \
                                                      unzip \
                                                      rubygems
RUN pip install PIL
RUN gem install sass --version '3.3.4'
RUN cd /opt; curl -O -s https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.5.zip && \
    unzip -qq google_appengine_1.9.5.zip && rm google_appengine_1.9.5.zip
ENV PATH /opt/google_appengine:$PATH
ADD . /opt/ocargo/
RUN chmod +x /opt/ocargo/deploy.sh
CMD ["/opt/ocargo/deploy.sh"]
