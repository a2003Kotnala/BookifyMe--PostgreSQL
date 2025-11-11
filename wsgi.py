from app import create_app, db
from app.models.user import User

app = create_app()

def initialize_database():
    """Initialize database tables and admin user"""
    try:
        print("🔄 Creating database tables...")
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Check if admin user exists
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
            
    except Exception as e:
        print(f"❌ Database setup error: {e}")

# Initialize database when app starts (Flask 2.3+ compatible)
with app.app_context():
    initialize_database()

if __name__ == '__main__':
    print("🚀 Starting BookifyMe Backend Server...")
    app.run(debug=True, port=5000)