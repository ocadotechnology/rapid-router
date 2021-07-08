# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install git for pip dependencies from repositories
RUN apt-get -y update
RUN apt-get -y install git

# Add permission to write tothe install dirs
# RUN easy_install

# Setup pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install pipenv

WORKDIR /app
COPY . /app

# Install pip dependencies
RUN python -m pipenv install --dev --system

RUN ./run

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'rapid-router'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "example_project.example_project.wsgi"]
