FROM platzi/python3-pycharm

RUN mkdir /app/
COPY requirements.txt /tmp/requirements.txt
COPY common.txt /tmp/common.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir /tmp/authorized_keys/
WORKDIR /app/project
