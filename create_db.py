import psycopg2
import sys

def create_database():
    # Try common passwords
    passwords = ['', 'postgres', 'password', 'admin', '123456']
    
    for pwd in passwords:
        try:
            print(f"Trying password: '{pwd}'")
            conn = psycopg2.connect(
                dbname='postgres',
                user='postgres',
                password=pwd,
                host='localhost',
                port='5432'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            
            # Try to create database
            try:
                cursor.execute("CREATE DATABASE bookifyme;")
                print("✅ Database 'bookifyme' created successfully!")
            except psycopg2.Error as e:
                if "already exists" in str(e):
                    print("ℹ️ Database 'bookifyme' already exists")
                else:
                    print(f"⚠️ {e}")
            
            cursor.close()
            conn.close()
            print(f"✅ Connected successfully with password: '{pwd}'")
            print(f"📝 Use this in your .env file: DATABASE_URL=postgresql://postgres:{pwd}@localhost:5432/bookifyme")
            return
            
        except psycopg2.Error as e:
            print(f"❌ Failed with password '{pwd}': {e}")
            continue
    
    print("\n🔧 Manual password reset required.")
    print("Follow these steps:")
    print("1. Open Services (Win+R → services.msc)")
    print("2. Find 'PostgreSQL' service and stop it")
    print("3. Find pg_hba.conf (usually in C:\\Program Files\\PostgreSQL\\XX\\data\\)")
    print("4. Change 'md5' to 'trust' for local connections")
    print("5. Restart PostgreSQL service")
    print("6. Then you can connect without password and reset it")

if __name__ == '__main__':
    create_database()