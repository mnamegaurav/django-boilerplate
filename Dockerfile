FROM python:3.11

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-dev \
    build-essential \
    nano \
    python3-pip \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    nginx \
    curl \
    gdal-bin \
    libffi-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    libpango-1.0-0 \
    python3-cffi \
    python3-brotli \
    postgis \
    daphne \
    redis-server \
    graphviz \
    graphviz-dev
    
# copy project
COPY . /code/

# install dependencies
COPY ./requirements.txt /code/
RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 8000