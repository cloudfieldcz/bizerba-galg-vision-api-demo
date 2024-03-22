FROM python:3.9-slim-buster

LABEL app=galg-vision-api-demo

WORKDIR /build

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qyy \
	ffmpeg libsm6 libxext6 \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 10003
ENTRYPOINT [ "python", "main.py" ]
