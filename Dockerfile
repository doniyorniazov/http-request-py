FROM --platform=linux/amd64 python:3.8-slim as build

ENV HOST=http://host.com
ENV COMPANY=demo
ENV PORT=8002
ENV SLEEP=10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python","-u", "request.py"]
