import psycopg2
from app import create_app, db
from app.models.user import User
import os

def setup_database():
    print("🚀 Setting up BookifyMe with PostgreSQL...")
    
    # Step 1: Test connection and create database
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='Ankit@1245',
            host='localhost',
            port='5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        try:
            cursor.execute("CREATE DATABASE bookifyme;")
            print("✅ Database 'bookifyme' created!")
        except Exception as e:
            if "already exists" in str(e):
                print("ℹ️ Database 'bookifyme' already exists")
            else:
                print(f"⚠️ {e}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Database creation failed: {e}")
        return False
    
    # Step 2: Initialize tables
    try:
        app = create_app()
        with app.app_context():
            print("🔄 Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Create default admin user
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
                    print("✅ Default admin user created")
                    print("   Email: admin@bookifyme.com")
                    print("   Password: admin123")
            except Exception as e:
                print(f"⚠️ Could not create admin user: {e}")
                db.session.rollback()
                
        return True
        
    except Exception as e:
        print(f"❌ Table creation failed: {e}")
        return False

if __name__ == '__main__':
    setup_database()