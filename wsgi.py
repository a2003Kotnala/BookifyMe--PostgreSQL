from app import create_app, db
from config import debug_database_config

# Debug database configuration first
debug_database_config()

app = create_app()

@app.before_first_request
def create_tables():
    """Create database tables on startup"""
    try:
        print("🔄 Creating database tables...")
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Check if admin user exists
        from app.models.user import User
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

if __name__ == '__main__':
    print("🚀 Starting BookifyMe Backend Server...")
    app.run(debug=True, port=5000)