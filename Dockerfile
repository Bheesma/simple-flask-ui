FROM python:3.6
LABEL maintainer="prakash"
COPY . /src
WORKDIR /src/src
ENV FLASK_APP=base.py
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]