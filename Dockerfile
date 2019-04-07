FROM python:3-alpine

RUN mkdir -p /opt/workdir

WORKDIR /opt/workdir

COPY ./entrypoint.sh /entrypoint.sh
COPY ./driver.py /opt/workdir
COPY ./requirements.txt /opt/workdir

RUN pip install -r /opt/workdir/requirements.txt

ENTRYPOINT /entrypoint.sh
