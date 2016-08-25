FROM python:3

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tar build-essential

RUN mkdir /app

COPY requirements.txt /tmp/requirements.txt
COPY common.txt /tmp/common.txt

RUN pip install -r /tmp/requirements.txt

RUN rm -f /tmp/requirements.txt

RUN apt-get autoclean

COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app
ENTRYPOINT ["/entrypoint.sh"]

