"""
Database Loader

Responsible for persisting fully scraped Article objects into the TechPulse
relational database.

Responsibilities:
- Prevent duplicate articles.
- Insert new articles.
- Create or reuse related entities (source, authors, companies, technologies, tags).
- Populate bridge tables.
- Maintain transactional consistency.

This class is the only component responsible for writing data to the database.
"""
from scrapers.common.database import Database

class DatabaseLoader():

    def __init__(self, db:Database):
        self.db = db
        self.cursor = db.get_cursor()

    def load_articles(self, articles, source_metadata):
        '''
        Public Point of Entry.
        Load all the articles into the database.
        '''

        for article in articles:
            try:
                self._load_single_article(article, source_metadata)
            except Exception as e:
                self.db.rollback()
                raise e
            

    def _load_single_article(self, article, source_metadata):

        # ArticleExists ?
        # Yes return article_id
        # Insert The article
        # Return article id

        exists = self._article_exists(article.article_url)

        if exists:
            return exists[0]
        
        source_id = self._get_or_create_source(source_metadata)

        author_ids = []

        for author in article.authors:
            author_id = self._get_or_create_author(source_id, author)
            author_ids.append(author_id)

        company_ids = []

        for company in article.companies:
            company_id = self._get_or_create_company(company)
            company_ids.append(company_id)

        technology_ids = []

        for technology in article.technologies:
            technology_id = self._get_or_create_technology(technology)
            technology_ids.append(technology_id)

        tag_ids = []

        for tag in article.tags:
            tag_id = self._get_or_create_tag(tag)
            tag_ids.append(tag_id)


        category_id = self._get_or_create_category(article.category)
        
        article_id = self._insert_article(article, source_id, category_id)

        self._insert_article_authors(article_id, author_ids)

        self._insert_article_companies(article_id, company_ids)

        self._insert_article_technologies(article_id, technology_ids)

        self._insert_article_tags(article_id, tag_ids)
        
        self.db.commit()

        return article_id

        
    def _article_exists(self, article_url):

        self.cursor.execute("SELECT article_id FROM articles WHERE article_url =  %s", (article_url,))
        result = self.cursor.fetchone()

        return result

    def _insert_article(self, article, source_id, category_id):

        values_of_article = (
        article.article_url,
        source_id,
        category_id,
        article.title,
        article.summary,
        article.content,
        article.published_at,
        article.word_count,
        article.reading_time,
        article.content_hash
        )

        self.cursor.execute("INSERT INTO articles (article_url, source_id, category_id, title, summary, content, published_at, word_count, reading_time, content_hash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values_of_article)

        return self.cursor.lastrowid




    def _get_or_create_source(self, source_metadata):

        self.cursor.execute("SELECT source_id FROM sources WHERE source_name=%s and website_url=%s", (source_metadata['source_name'], source_metadata['website_url']))
        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:
            self.cursor.execute("INSERT INTO sources (source_name, website_url) VALUES (%s, %s)", (source_metadata['source_name'], source_metadata['website_url']))

            return self.cursor.lastrowid



    def _get_or_create_category(self, category):

        self.cursor.execute("SELECT category_id FROM categories WHERE category_name = %s", (category,))
        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:
            self.cursor.execute("INSERT INTO categories(category_name) VALUES (%s)", (category,))

            return self.cursor.lastrowid


    def _get_or_create_author(self, source_id, display_name):

        self.cursor.execute("SELECT author_id FROM authors WHERE source_id = %s and display_name = %s", (source_id, display_name))

        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:

            self.cursor.execute("INSERT INTO authors (source_id, display_name) VALUES (%s, %s)", (source_id, display_name))

            return self.cursor.lastrowid
        
    def _get_or_create_company(self, company):

        self.cursor.execute("SELECT company_id FROM companies WHERE company_name = %s", (company,))

        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:

            self.cursor.execute("INSERT INTO companies (company_name) VALUES (%s)", (company,))

            return self.cursor.lastrowid
        
    def _get_or_create_technology(self, technology):

        self.cursor.execute("SELECT technology_id FROM technologies WHERE technology_name = %s", (technology,))

        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:
            
            self.cursor.execute("INSERT INTO technologies (technology_name) VALUES (%s)", (technology,))

            return self.cursor.lastrowid

    def _get_or_create_tag(self, tag):

        self.cursor.execute("SELECT tag_id FROM tags WHERE tag_name = %s", (tag,))

        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:

            self.cursor.execute("INSERT INTO tags (tag_name) VALUES (%s)", (tag,))

            return self.cursor.lastrowid


    def _insert_article_authors(self, article_id, author_ids):
        '''
        Insert realtionships between an article and its authors.
        '''
        for author_id in author_ids:
            self.cursor.execute("INSERT INTO article_authors (article_id, author_id) VALUES (%s, %s)", (article_id, author_id))


    def _insert_article_companies(self, article_id, company_ids):
        '''
        Insert relationships between an article and its companies
        '''

        for company_id in company_ids:
            self.cursor.execute("INSERT INTO article_companies (article_id, company_id) VALUES (%s, %s)", (article_id, company_id))

    def _insert_article_technologies(self, article_id, technology_ids):
        '''
        Insert the relationships between the article and its technologies
        '''
        
        for technology_id in technology_ids:
            self.cursor.execute("INSERT INTO article_technologies (article_id, technology_id) VALUES (%s, %s)", (article_id, technology_id))

    def _insert_article_tags(self, article_id, tag_ids):
        '''
        Insert the relationships between the article and its tags
        '''

        for tag_id in tag_ids:
            self.cursor.execute("INSERT INTO article_tags (article_id, tag_id) VALUES (%s, %s)", (article_id, tag_id))

