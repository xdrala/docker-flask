from multiprocessing import cpu_count

# http://docs.gunicorn.org/en/stable/design.html#how-many-workers
workers = cpu_count() * 2 + 1

# Bind to 0.0.0.0 to allow external access
bind = '0.0.0.0:8000'

# Eventlet as worker class
worker_class = 'eventlet'

# Log to stdout
accesslog = '-'

# 30s of timeout
timeout = 30
