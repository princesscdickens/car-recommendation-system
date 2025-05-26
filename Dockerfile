# Pull Python from official Docker repo
FROM python:3.11-slim AS base-recommendation-system

WORKDIR /app

COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Create image for production
FROM base-recommendation-system AS prod-recommendation-system

WORKDIR /app

RUN ./manage.py migrate cars

CMD ["uwsgi", "--ini", "uwsgi.ini"]

# NGINX image for production
FROM nginx:1.23-alpine AS prod-nginx

WORKDIR /app

COPY nginx.conf /etc/nginx/nginx.conf
COPY host.conf /etc/nginx/conf.d/host.conf
COPY uwsgi_params /etc/nginx/uwsgi_params


