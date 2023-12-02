FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "/app/manage.py", "runserver", "0.0.0.0:8000" ]