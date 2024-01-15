# Pull Python from official Docker repo
FROM python:latest AS base-recommendation-system

COPY . ./

RUN pip install --upgrade pip && pip install -r requirements.txt

# Create image for production
FROM base-recommendation-system AS prod-recommendation-system

CMD ["uwsgi", "--ini", "uwsgi.ini"]

