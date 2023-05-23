FROM python:3.12.0a7-alpine3.18

RUN pip install Flask
RUN pip install pymongo
RUN pip install -U flask-cors
RUN pip install python-dotenv
