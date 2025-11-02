import psycopg2

# --- Database connection details ---
DB_HOST = "database-1.cncm40u8c3il.ap-south-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Samitha0130"

# --- Connect to PostgreSQL RDS ---
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL RDS successfully")

    # --- Create table if not exists ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            image_url TEXT
        );
    """)
    conn.commit()
    print("✅ Table 'courses' is ready")

    # --- Insert sample course data with S3 image URLs ---
    courses = [
        (
            "Python Basics",
            "Learn Python step by step with examples",
            "https://coursecomplex.s3.ap-south-1.amazonaws.com/python.png"
        ),
        (
            "Machine Learning 101",
            "Introduction to ML algorithms and concepts",
            "https://coursecomplex.s3.ap-south-1.amazonaws.com/springboot.png"
        ),
        (
            "AWS for Beginners",
            "Get started with AWS cloud fundamentals",
            "https://coursecomplex.s3.ap-south-1.amazonaws.com/aws.png"
        )
    ]

    for course in courses:
        cursor.execute(
            "INSERT INTO courses (title, description, image_url) VALUES (%s, %s, %s)",
            course
        )

    conn.commit()
    print("✅ Sample data inserted successfully")

except Exception as e:
    print("❌ Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("🔒 Connection closed")
