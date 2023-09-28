FROM python:3.8-slim

ENV HOST=http://host.com
ENV COMPANY=demo
ENV SLEEP=10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "request.py"]
