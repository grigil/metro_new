FROM python:3.9
WORKDIR app/
RUN apt update -y
RUN apt install -y g++ python3-dev python3-pip libc-dev
COPY requirements.txt .
RUN pip install -r requirements.txt