FROM python:3

WORKDIR /app

ADD . .

RUN pip install -U Flask

CMD ["python", "./main.py"]