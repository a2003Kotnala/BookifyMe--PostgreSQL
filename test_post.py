import psycopg2
from urllib.parse import quote

def test_connection():
    try:
        # Test with direct connection
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='Ankit@1245',  # Your actual password
            host='localhost',
            port='5432'
        )
        print("✅ Direct PostgreSQL connection successful!")
        
        # Create database
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
        
        # Test connection to the new database
        conn = psycopg2.connect(
            dbname='bookifyme',
            user='postgres',
            password='Ankit@1245',
            host='localhost',
            port='5432'
        )
        print("✅ Connection to 'bookifyme' database successful!")
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == '__main__':
    test_connection()