FROM python:3.5.2

RUN pip3 install flask connexion

ADD ./script /flask-demo

EXPOSE 5000

CMD ["python", "-u", "/flask-demo/app.py"]

