# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# RUN apk update 
RUN apk add --virtual build-deps gcc python3-dev musl-dev 
# RUN pip install psycopg2 
RUN apk add jpeg-dev zlib-dev libjpeg 
RUN pip install Pillow 
RUN apk del build-deps

# install dependencies
# RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy project
COPY . .