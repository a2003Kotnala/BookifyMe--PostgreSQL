#!/bin/bash

echo "🚀 Starting BookifyMe Backend..."

# Run database setup
echo "🔧 Running database setup..."
python database_setup.py

# Start Gunicorn
echo "🐍 Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:5000 wsgi:app