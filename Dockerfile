FROM python:latest

RUN pip install flask

ADD ./script /flask-demo

EXPOSE 5000

CMD ["python", "-u", "/flask-demo/hello.py"]

