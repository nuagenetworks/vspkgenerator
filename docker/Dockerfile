FROM python:2.7-alpine

RUN apk add git 
RUN pip install configparser && pip install gitpython requests future jinja2 colorama
RUN mkdir /build
WORKDIR /build
ENTRYPOINT ["sh", "/build/build.sh"]
COPY build.sh /build
RUN chmod 777 /build/build.sh
