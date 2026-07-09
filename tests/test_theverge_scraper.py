from scrapers.theverge.scraper import TheVergeScraper


def main():

    scraper = TheVergeScraper()

    articles = scraper.scrape()

    print(f"Scraped {len(articles)} articles.")

    if articles:
        print(articles[0])


if __name__ == "__main__":
    main()