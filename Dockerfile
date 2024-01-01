# Pull Python from official Docker repo
FROM python:3.9.18 AS base-recommendation-system

COPY . ./

RUN pip install --upgrade pip && pip install -r requirements.txt
