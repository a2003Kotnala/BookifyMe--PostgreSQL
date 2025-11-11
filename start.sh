#!/bin/bash

echo "🚀 Starting BookifyMe Backend..."
echo "🔧 Running database setup..."
python database_setup.py

echo "🐍 Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:$PORT wsgi:app