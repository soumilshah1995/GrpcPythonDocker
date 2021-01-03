FROM gcr.io/google_appengine/python:latest

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "grpcserver/server.py"]