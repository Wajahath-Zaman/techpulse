from src.scrapers.common.database import Database

def main():
    db = Database()

    try:
        db.connect()

        print("Database connected Successfully.")

        cursor = db.get_cursor()
        cursor.execute("SELECT 1")

        print(cursor.fetchone())

    finally:
        db.close()

        print("Connection Closed.")


if __name__ == "__main__":
    main()
