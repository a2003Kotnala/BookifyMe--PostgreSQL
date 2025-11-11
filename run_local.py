from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    print("🚀 Starting BookifyMe Backend with PostgreSQL...")
    print("📊 Database: PostgreSQL (localhost:5432/bookifyme)")
    print("🔐 User: postgres")
    print("🌐 Server: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)