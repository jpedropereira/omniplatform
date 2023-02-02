FROM python:3.10.6-slim-buster
ENV PYTHONUNBUFFERED=1
EXPOSE 9000
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /code/
WORKDIR /code/omniplatform
