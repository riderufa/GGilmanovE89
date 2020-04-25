FROM python:3.6-alpine




ADD . /
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# COPY ./app/app.py /app/app.py
# COPY ./app/main.py /app/main.py
# COPY ./app/config.py /app/config.py
# COPY ./app/view.py /app/view.py
# COPY ./app/consumer.py /app/consumer.py
# COPY ./app/flask_celery.py /app/flask_celery.py
# COPY ./app/forms.py /app/forms.py
# COPY ./app/models.py /app/models.py
# COPY ./app/templates/index.html /app/templates/index.html
# COPY ./app/templates/base.html /app/templates/base.html
# COPY ./app/templates/results.html /app/templates/results.html
# COPY ./app/templates/add_site.html /app/templates/add_site.html


RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install psycopg2-binary



# ENTRYPOINT celery -A app worker --concurrency=20 --loglevel=DEBUG