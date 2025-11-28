import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="appdb",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )

def list_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, email FROM users ORDER BY id;")
    rows = cur.fetchall()

    print("\nUsers in database:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def add_user(name, email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
        (name, email)
    )

    new_id = cur.fetchone()[0]
    conn.commit()

    print(f"Inserted new user with id = {new_id}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    list_users()
    add_user("Daniel", "daniel@example.com")
    list_users()
