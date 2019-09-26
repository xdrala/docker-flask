FROM python:3.6-stretch

# Software versions
ENV NGINX_VERSION=1.17.2-1~stretch \
    GUNICORN_VERSION=19.9.0 \
    EVENTLET_VERSION=0.25.1 \
    FLASK_VERSION=1.1.1 \
    APP_ENVIRONMENT=production

# Install nginx and supervisor
RUN echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list \
    && wget https://nginx.org/keys/nginx_signing.key -O - | apt-key add - \
    && apt-get update && apt-get install -y nginx=$NGINX_VERSION \
                                            supervisor \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
RUN pip install -U pip \
    && pip install gunicorn==$GUNICORN_VERSION \
                   eventlet==$EVENTLET_VERSION \
                   Flask==$FLASK_VERSION

# Conf Nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY conf/nginx.nginx /etc/nginx/conf.d/default.conf

# Conf Supervisor
COPY conf/supervisor/ /etc/supervisor/conf.d/

# Conf Gunicorn
COPY conf/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py

# Sample app
COPY app /app

# 80 for HTTP
EXPOSE 80

# Run all with supervisord
CMD /usr/bin/supervisord
