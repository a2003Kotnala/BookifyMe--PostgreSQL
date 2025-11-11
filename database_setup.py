import os
from app import create_app, db
from app.models.user import User
from app.models.book import Book
from app.models.bookshelf import Bookshelf
from app.models.group import ReadingGroup, GroupMember

def init_db():
    app = create_app()
    with app.app_context():
        try:
            # Test database connection
            db.session.execute('SELECT 1')
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
                
        except Exception as e:
            print(f"❌ Database setup failed: {e}")
            raise

if __name__ == '__main__':
    init_db()