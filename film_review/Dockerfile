FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code
RUN python -m pip install --upgrade pip && pip install -r requirements.txt