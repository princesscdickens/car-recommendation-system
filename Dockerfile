# Pull Python from official Docker repo
FROM python:latest AS base-recommendation-system

COPY . ./

RUN pip install --upgrade pip && pip install -r requirements.txt
