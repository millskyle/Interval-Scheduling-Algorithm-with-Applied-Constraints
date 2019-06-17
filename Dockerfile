FROM python:2-alpine

RUN apk --no-cache add postgresql-libs \
  libffi \
  libxml2 \
  libxslt

RUN apk --no-cache add --virtual .build-deps build-base \
  postgresql-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apk --no-cache del .build-deps

COPY . .

WORKDIR /usr/src/app/src/webserver

ENTRYPOINT ["python"]
CMD ["webserver.py"]
