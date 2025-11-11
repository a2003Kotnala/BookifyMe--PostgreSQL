import os
import time
from sqlalchemy import text  # ADD THIS IMPORT
from app import create_app, db
from app.models.user import User
from app.models.book import Book
from app.models.bookshelf import Bookshelf
from app.models.group import ReadingGroup, GroupMember

def init_db():
    app = create_app()
    with app.app_context():
        max_retries = 5
        for attempt in range(max_retries):
            try:
                # Test database connection - FIXED for SQLAlchemy 2.0
                db.session.execute(text('SELECT 1'))  # WRAP IN text()
                print("✅ Database connection successful!")
                
                # Create all tables
                print("🔄 Creating database tables...")
                db.create_all()
                print("✅ Database tables created successfully!")
                
                # Optional: Add a default admin user for testing
                try:
                    admin = User.query.filter_by(email='admin@bookifyme.com').first()
                    if not admin:
                        admin = User(
                            name='Admin User',
                            email='admin@bookifyme.com'
                        )
                        admin.set_password('admin123')
                        db.session.add(admin)
                        db.session.commit()
                        print("✅ Default admin user created (email: admin@bookifyme.com, password: admin123)")
                except Exception as e:
                    print(f"⚠️ Could not create admin user: {e}")
                    db.session.rollback()
                
                return
                    
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"❌ Database setup attempt {attempt + 1} failed: {e}")
                    print("🔄 Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    print(f"❌ Database setup failed after {max_retries} attempts: {e}")
                    raise

if __name__ == '__main__':
    init_db()