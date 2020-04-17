FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r req.txt
RUN pip install gunicorn
RUN python manage.py collectstatic --noinput


