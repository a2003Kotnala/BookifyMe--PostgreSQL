#!/bin/bash

echo "🚀 Starting BookifyMe Backend..."

# Wait for the database to be ready (optional, but recommended)
echo "🔧 Checking database connection..."
python -c "
import time
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

database_url = os.getenv('DATABASE_URL')
if database_url:
    # Replace postgresql:// with postgres:// for SQLAlchemy
    if database_url.startswith('postgresql://'):
        database_url = database_url.replace('postgresql://', 'postgres://', 1)
    
    engine = create_engine(database_url)
    
    for i in range(10):
        try:
            with engine.connect() as conn:
                print('✅ Database connection successful')
                break
        except OperationalError as e:
            if i == 9:
                print('❌ Database connection failed after 10 attempts')
                raise e
            print(f'⏳ Waiting for database... attempt {i+1}/10')
            time.sleep(2)
"

# Run database setup
echo "🔧 Running database setup..."
python database_setup.py

# Start Gunicorn
echo "🐍 Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:5000 wsgi:app