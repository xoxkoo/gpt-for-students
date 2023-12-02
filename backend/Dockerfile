FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Run migrations during the build process
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

# CMD to start the application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]