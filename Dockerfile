FROM python:latest

RUN pip3 install pymongo
RUN pip3 install python-dotenv

WORKDIR /app

COPY *.py ./

CMD [ "python", "./main.py"]
