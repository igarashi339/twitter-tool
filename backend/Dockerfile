FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="/code/twitter_tool"
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt