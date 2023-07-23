FROM python:latest

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY bin/ /app

WORKDIR /app

RUN apt-get update \
    && apt install unixodbc-dev -y

RUN pip install -r requirements.txt

CMD ["python", "/app/app.py"]
