from src.scrapers.common.database_loader import DatabaseLoader
from src.scrapers.common.database import Database


def main():

    db = Database()
    loader = DatabaseLoader(db)

    new_entry = {"source_name": "Youtube", "website_url": "https://www.youtube.com"}

    try:
        loader._get_or_create_source("twitter", "https://www.twitter.com")
    finally:
        print("executed")


if __name__ == "__main__":
    main()