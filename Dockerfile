FROM python:3.9-slim-buster

RUN mkdir build

WORKDIR /build


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

EXPOSE 10003

ENTRYPOINT [ "python", "main.py"]