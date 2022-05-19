#!/bin/sh

while true; do
    flask db upgrade && break || { echo Upgrade command failed, retrying in 5 secs...; sleep 5; }
done

# flask translate compile
#exec gunicorn --workers 2 -b :5000 --access-logfile - --error-logfile - app:app
exec flask run --host 0.0.0.0 -p 5000
