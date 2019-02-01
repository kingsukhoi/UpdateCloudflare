FROM python:3-alpine

RUN mkdir -p /opt/workdir

WORKDIR /opt/workdir

COPY ./driver.py /opt/workdir

ENTRYPOINT python /opt/workdir/driver.py
