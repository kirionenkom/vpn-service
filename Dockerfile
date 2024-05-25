FROM python:3.8-slim-buster
MAINTAINER Mikhail Kirionenko 'misha.kirionenko03@gmail.com'
WORKDIR /vpn-service
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]