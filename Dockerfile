FROM python:3.8.5

RUN apt-get update && apt-get install -y  python3-dev default-libmysqlclient-dev 

RUN mkdir /code
WORKDIR /code
ADD requirment.txt /code/
RUN pip install -r requirment.txt
ADD . /code/

COPY docker-entrypoint.sh /usr/local/bin
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["docker-entrypoint.sh"]