FROM python:3.8-slim

MAINTAINER Avantika Singh "as13594@nyu.edu"

RUN apt-get update -y && \
	apt-get install -y python-pip python-dev && \
	apt-get install -y build-essential

EXPOSE 5000

COPY code/requirements.txt /app/requirements.txt
COPY code/main.py /app/main.py
COPY code/imagenet /app/imagenet

WORKDIR /app
RUN pip install -r requirements.txt


CMD python main.py -a alexnet -b 8 --epochs 1 --lr 0.01 imagenet