#!/bin/sh

# Wait for DB to be ready
echo "Waiting for Postgres..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --log-level=info
