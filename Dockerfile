FROM python:3


WORKDIR /app

COPY . .

EXPOSE 5000

ENTRYPOINT ['python3','main.py']