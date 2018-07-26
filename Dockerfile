FROM python:3.6-alpine3.8

LABEL maintainer="Akshay Raj Gollahalli <akshay.gollahalli@aut.ac.nz>"

# Update, install the required packages and clean downloaded package
RUN apk update && \
    apk upgrade && \
    rm -rf /var/cache/apk/*

# Update pip
RUN pip install -U pip

COPY . /opt/app

WORKDIR /opt/app

# Install requirements
RUN set -ex && apk add --no-cache --virtual .requirements-deps  \
		bzip2-dev \
		coreutils \
		dpkg-dev dpkg \
		expat-dev \
		findutils \
		gcc \
		gdbm-dev \
		libc-dev \
		libffi-dev \
		libnsl-dev \
		libressl \
		libressl-dev \
		libtirpc-dev \
		linux-headers \
		make \
		ncurses-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		xz-dev \
		zlib-dev \
# add build deps before removing fetch deps in case there's overlap
    && pip install -r requirements.txt \
    && apk del .requirements-deps

EXPOSE 8000

CMD ["gunicorn", "-c", "/opt/app/gunicorn.conf.py", "neucube_api.wsgi"]