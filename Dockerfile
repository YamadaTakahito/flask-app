FROM python:3.6.6-slim-stretch

ENV ROOT_PATH /app

RUN mkdir $ROOT_PATH

WORKDIR $ROOT_PATH

COPY requirements.txt $ROOT_PATH/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

