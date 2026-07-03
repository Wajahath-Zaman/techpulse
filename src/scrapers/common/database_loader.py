from src.scrapers.common.database import Database



class DatabaseLoader():
    def __init__(self, db: Database):
        self.db = db
        db.connect()
        self.cursor = db.get_cursor()

    def load_articles(self, articles):
        '''
        Main entry point.
        Loops through all articles
        '''
        pass

    def _load_single_article(self, article):
        """
        Loads one single article into the database
        """
        pass

    def _resolve_entities(self, article):
        """"
        Resolve or create:
        - Source
        - Category
        - Authors
        - Companies
        - Technologies
        - Tags
        """
        source_id = self._get_or_create_source(article.source)
        print(source_id)

    def _insert_article(self, article):
        pass

    def _insert_bridge_table(self, article):
        pass

    def _get_or_create_source(self, source_name, website_url, rss_feed_url=None, country=None, language=None):

        self.cursor.execute("SELECT * FROM sources WHERE source_name = %s", (source_name,))
        result = self.cursor.fetchone()
    
        if result:
            return result[0]
        
        else:
            self.cursor.execute("INSERT INTO sources (source_name, website_url) VALUES (%s, %s)", (source_name, website_url, rss_feed_url, country, language))
            self.db.commit(),

            return self.cursor.lastrowid