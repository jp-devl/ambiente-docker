FROM python:slim

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
    
COPY ./app .
ENTRYPOINT [ "flask","run", "--debug","--host=0.0.0.0" ]