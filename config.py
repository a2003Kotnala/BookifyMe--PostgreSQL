import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key-change-in-production'
    
    # PostgreSQL configuration
    DATABASE_URL = os.environ.get('DATABASE_URL', '')
    
    # Handle both postgres:// and postgresql:// URLs for Render
    if DATABASE_URL:
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Local development fallback
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ankit%401245@localhost:5432/bookifyme'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT Configuration
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    
    # Google Books API
    GOOGLE_BOOKS_API_KEY = os.environ.get('GOOGLE_BOOKS_API_KEY') or 'AIzaSyDfWNJLVlecyOYbfDtce7BQwmbO0zg9QBc'
    GOOGLE_BOOKS_BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    
    # CORS
    FRONTEND_URL = os.environ.get('FRONTEND_URL') or 'http://127.0.0.1:5500'
    
    # Email Configuration
    SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
    FROM_EMAIL = os.environ.get('FROM_EMAIL', 'noreply@bookifyme.com')

# Debug: Print database configuration (safe version - hides password)
def debug_database_config():
    config = Config()
    db_uri = config.SQLALCHEMY_DATABASE_URI
    if db_uri:
        # Hide password in logs for security
        safe_uri = db_uri
        if '@' in db_uri:
            parts = db_uri.split('@')
            user_part = parts[0]
            if ':' in user_part:
                user_pass = user_part.split(':')
                if len(user_pass) >= 3:  # postgresql://user:pass@host
                    safe_uri = f"postgresql://{user_pass[0]}:****@{parts[1]}"
        print(f"🔧 Database Config: {safe_uri}")
        print(f"🔧 Using DATABASE_URL: {'Yes' if os.environ.get('DATABASE_URL') else 'No'}")
    return config

# Run debug when module is loaded directly
if __name__ == '__main__':
    debug_database_config()