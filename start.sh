#!/bin/bash

echo "🚀 Starting BookifyMe Backend..."

# Debug environment
echo "🔧 Environment Debug:"
python -c "
import os
print('DATABASE_URL:', 'SET' if os.getenv('DATABASE_URL') else 'NOT SET')
print('SECRET_KEY:', 'SET' if os.getenv('SECRET_KEY') else 'NOT SET')
print('JWT_SECRET_KEY:', 'SET' if os.getenv('JWT_SECRET_KEY') else 'NOT SET')
"

# Wait for database to be ready
echo "🔧 Checking database connection..."
python -c "
import time
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

database_url = os.getenv('DATABASE_URL')
if database_url:
    # Replace postgres:// with postgresql:// for SQLAlchemy
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    engine = create_engine(database_url)
    
    for i in range(10):
        try:
            with engine.connect() as conn:
                print('✅ Database connection successful')
                break
        except OperationalError as e:
            if i == 9:
                print('❌ Database connection failed after 10 attempts')
                print(f'Error: {e}')
                raise e
            print(f'⏳ Waiting for database... attempt {i+1}/10')
            time.sleep(2)
else:
    print('❌ DATABASE_URL environment variable not set')
"

# Run database setup
echo "🔧 Running database setup..."
python database_setup.py

# Start Gunicorn
echo "🐍 Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:5000 wsgi:app