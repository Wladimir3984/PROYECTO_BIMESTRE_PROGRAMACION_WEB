# syntax=docker/dockerfile:1
FROM python:3.12.0a7-alpine3.17
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/


RUN \
    pip install --no-cache-dir --upgrade pip && \
    apk --no-cache add \
    # Pillow dependencies
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    libimagequant-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache  gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir

RUN apk add bash

COPY . /code/

