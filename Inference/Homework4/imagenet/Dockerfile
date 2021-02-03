FROM ubuntu:16.04
FROM mapler/pytorch-cpu
FROM python:3.8-slim

MAINTAINER Avantika Singh "as13594@nyu.edu"

RUN apt-get update -y && \
	apt-get install -y python-pip python-dev && \
	apt-get install -y build-essential

EXPOSE 5000
#Using requirements file
COPY app/requirements.txt /app/requirements.txt

#Main files
COPY app/flask_main.py /temp/flask_main.py
COPY app/model_best.pth.tar /temp/model_best.pth.tar

#Prediction files
COPY app/predict_main.py /temp/predict_main.py

#Class files
COPY app/imagenet_classes_index.txt /temp/imagenet_classes_index.txt

#HTML Files
COPY app/static/upload.js temp/static/upload.js
COPY app/templates/home_page.html temp/templates/home_page.html

COPY app/uploads temp/uploads
WORKDIR /temp

RUN pip install --upgrade pip

RUN pip install torch
RUN pip install torchvision
RUN pip install flask
RUN pip install pillow

ENTRYPOINT ["python"]

CMD ["flask_main.py"]
