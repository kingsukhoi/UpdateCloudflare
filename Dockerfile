FROM python:3-alpine

RUN mkdir -p /opt/workdir

WORKDIR /opt/workdir

VOLUME /opt/workdir/file.csv

COPY ./driver.py /opt/workdir

ENTRYPOINT python /opt/workdir/driver.py /opt/workdir/file.csv

