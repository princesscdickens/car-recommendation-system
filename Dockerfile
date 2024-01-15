# Pull Python from official Docker repo
FROM python:latest AS base-recommendation-system

COPY . ./

RUN pip install --upgrade pip && pip install -r requirements.txt

# Create image for production
FROM base-recommendation-system AS prod-recommendation-system

CMD ["uwsgi", "--ini", "uwsgi.ini"]

# NGINX image for production
FROM nginx:1.23-alpine AS prod-nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY host.conf /etc/nginx/conf.d/host.conf
COPY uwsgi_params /etc/nginx/uwsgi_params


