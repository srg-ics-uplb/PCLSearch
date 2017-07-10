############################################################
# Scrapy Development
############################################################

FROM ubuntu:16.04
LABEL maintainer="srg.ics.uplb.edu.ph"

RUN apt-get update

## Python Family
RUN apt-get install -qy python python-dev python-distribute python-pip ipython

## Scraping
RUN pip install --upgrade pip
RUN pip install beautifulsoup4 requests 
RUN apt-get install -qy libffi-dev libxml2-dev libxslt-dev lib32z1-dev libssl-dev

## Scrapy
RUN pip install lxml scrapy scrapyjs

RUN mkdir -p /usr/src/app 
WORKDIR /usr/src/app
COPY . /usr/src/app
