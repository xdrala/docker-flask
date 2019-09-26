FROM python:3.6-stretch

# Software versions
ENV GUNICORN_VERSION=19.9.0 \
    EVENTLET_VERSION=0.25.1 \
    FLASK_VERSION=1.1.1

# Install python packages
RUN pip install -U pip \
    && pip install gunicorn==$GUNICORN_VERSION \
                   eventlet==$EVENTLET_VERSION \
                   Flask==$FLASK_VERSION

# Conf Gunicorn
COPY conf/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py

# Sample app
COPY app /app

# Workdir for Gunicorn
WORKDIR /app

# 8000 for Gunicorn
EXPOSE 8000

# Run the app with Gunicorn
ENTRYPOINT gunicorn -c /etc/gunicorn/gunicorn.config.py run:app
