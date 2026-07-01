

USE techpulse;

-- Sources Table: Stores the metadata about technology news publishers.

CREATE TABLE sources (
	source_id INT PRIMARY KEY AUTO_INCREMENT,
	source_name VARCHAR(100) NOT NULL UNIQUE,
	website_url VARCHAR(500) NOT NULL UNIQUE,
	rss_feed_url VARCHAR(500) NULL UNIQUE,
	country VARCHAR(100) NULL,
	language CHAR(2) NOT NULL DEFAULT 'en',
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- Categories Table: It stores the list of standardized news categories used throughout the platform.

CREATE TABLE categories (
	category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Authors Table: This tables stores the list of authors for whom we have scraped the articles

CREATE TABLE authors (
	author_id INT PRIMARY KEY AUTO_INCREMENT,
    source_id INT NOT NULL,
    display_name VARCHAR(150) NOT NULL,
    profile_url VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_author_source
		FOREIGN KEY (source_id)
        REFERENCES sources(source_id),
        
	UNIQUE(source_id, display_name)
);


-- Companies table: This table stores the list of organisations mentioned in the article

CREATE TABLE companies (
	company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(150),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- Technologies table: This table stores the information about the technologies mentioned in the article

CREATE TABLE technologies (
	technology_id INT PRIMARY KEY AUTO_INCREMENT,
    technology_name VARCHAR(100),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tags table: This table will store the topics as tags for proper filtering og the articles

CREATE TABLE tags (
	tag_id INT PRIMARY KEY AUTO_INCREMENT,
    tag_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- Articles tables: This table will store all the information about different articles.

CREATE TABLE articles (
    article_id INT PRIMARY KEY AUTO_INCREMENT,
    article_url VARCHAR(500) NOT NULL UNIQUE,
    source_id INT NOT NULL,
    category_id INT NOT NULL,

    title VARCHAR(300) NOT NULL,
    summary TEXT,
    content LONGTEXT,

    published_at DATETIME,
    scraped_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    word_count INT,
    reading_time SMALLINT,

    content_hash CHAR(64) NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_articles_source
        FOREIGN KEY (source_id)
        REFERENCES sources(source_id),

    CONSTRAINT fk_articles_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
    );
    
    
-- BRIDGE TABLES ARE CREATED NOW.

CREATE TABLE article_authors (
    article_id INT NOT NULL,
    author_id INT NOT NULL,

    PRIMARY KEY (article_id, author_id),

    CONSTRAINT fk_article_authors_article
        FOREIGN KEY (article_id)
        REFERENCES articles(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_article_authors_author
        FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE article_companies (
    article_id INT NOT NULL,
    company_id INT NOT NULL,

    PRIMARY KEY (article_id, company_id),

    CONSTRAINT fk_article_companies_article
        FOREIGN KEY (article_id)
        REFERENCES articles(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_article_companies_company
        FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE article_technologies (
    article_id INT NOT NULL,
    technology_id INT NOT NULL,

    PRIMARY KEY (article_id, technology_id),

    CONSTRAINT fk_article_technologies_article
        FOREIGN KEY (article_id)
        REFERENCES articles(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_article_technologies_technology
        FOREIGN KEY (technology_id)
        REFERENCES technologies(technology_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE article_tags (
	article_id INT NOT NULL,
	tag_id INT NOT NULL,

	PRIMARY KEY (article_id, tag_id),

	CONSTRAINT fk_article_tags_article
		FOREIGN KEY (article_id)
		REFERENCES articles(article_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,

	CONSTRAINT fk_article_tags_tag
		FOREIGN KEY (tag_id)
		REFERENCES tags(tag_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);

 CREATE TABLE scrape_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    source_id INT NOT NULL,

    scrape_started_at TIMESTAMP NOT NULL,
    scrape_completed_at TIMESTAMP NULL,

    articles_found INT NOT NULL DEFAULT 0,
    articles_inserted INT NOT NULL DEFAULT 0,

    status ENUM('SUCCESS', 'FAILED', 'PARTIAL') NOT NULL,

    error_message TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_scrape_logs_source
        FOREIGN KEY (source_id)
        REFERENCES sources(source_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

