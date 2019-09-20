FROM centos:7

RUN yum install -y epel-release && yum install -y git python-pip 
RUN pip install configparser && pip install gitpython requests future jinja2 colorama
RUN mkdir /build
WORKDIR /build
ENTRYPOINT ["/build/build.sh"]
COPY build.sh /build
RUN chmod 777 /build/build.sh
