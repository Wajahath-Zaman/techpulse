#### In this md file we are going to demonstrate how we achieved the way we achieved it.

##### We will later summarize it.


### Phase I - Project Setup
- Create the project folder. --> Techpulse
- Initialized git.
- Created a virtual environment for python dependencies.
    - We created it using the command `python -m venv .venv`
    - We used it using the command --> `.venv\Scripts\activate`
- Inside the root folder we created the following architecture:
    ```text
    TechPulse/
    │
    ├── data/
    │   ├── raw/
    │   ├── processed/
    │   └── archive/
    │
    ├── scrapers/
    │   ├── common/
    │   └── sources/
    │
    ├── database/
    │
    ├── etl/
    │
    ├── analysis/
    │
    ├── dashboard/
    │
    ├── notebooks/
    │
    ├── reports/
    │
    ├── config/
    │
    ├── logs/
    │
    ├── tests/
    │
    └── docs/
    ```
    - Purpose of there folders:
    | Folder         | Purpose                      |
    | -------------- | ---------------------------- |
    | data/raw       | Original scraped data        |
    | data/processed | Cleaned datasets             |
    | data/archive   | Historical backups           |
    | scrapers       | All scraping scripts         |
    | database       | SQL scripts, ERD, schema     |
    | etl            | Data cleaning and loading    |
    | analysis       | Python analysis scripts      |
    | dashboard      | Tableau workbook and exports |
    | notebooks      | Jupyter notebooks            |
    | reports        | Generated reports            |
    | config         | Configuration files          |
    | logs           | Scraper and ETL logs         |
    | tests          | Unit tests                   |
    | docs           | Documentation and diagrams   |

    - The structure scales well when the project grows.

- Created the required essential files:
    1. README.md
    2. requirements.txt
    3. .gitignore
    4. LICENSE
    5. main.py
- Created the .gitignore and entered the text:
    ```gitignore
    # Virtual Environment
    .venv/

    # Python Cache
    __pycache__/
    *.pyc

    # Jupyter
    .ipynb_checkpoints/

    # VS Code
    .vscode/

    # Environment Variables
    .env

    # Logs
    logs/*.log

    # Data
    data/raw/*
    data/processed/*
    !data/raw/.gitkeep
    !data/processed/.gitkeep

    # OS
    .DS_Store
    Thumbs.db
    ```
- Sometimes the git doesn't track empty files:
    So we created .gitkeep files for different folders like:
    ```text
    data/raw/.gitkeep

    data/processed/.gitkeep

    data/archive/.gitkeep

    logs/.gitkeep

    reports/.gitkeep

    tests/.gitkeep
    ```
- Then we installed the required libraries for this entire project using the command:
```bash
pip install requests beautifulsoup4 pandas numpy sqlalchemy pymysql lxml python-dotenv tqdm matplotlib nltk spacy jupyter
```
    ```text
    | Package          | Purpose                                                  |
    | ---------------- | -------------------------------------------------------- |
    | `requests`       | Download web pages                                       |
    | `beautifulsoup4` | Parse HTML                                               |
    | `lxml`           | Faster HTML/XML parsing                                  |
    | `pandas`         | Clean and analyze data                                   |
    | `numpy`          | Numerical operations                                     |
    | `sqlalchemy`     | Connect Python to MySQL using an ORM or SQL layer        |
    | `pymysql`        | MySQL database driver                                    |
    | `python-dotenv`  | Load configuration from `.env` files                     |
    | `tqdm`           | Progress bars for long-running tasks                     |
    | `matplotlib`     | Data visualization during analysis                       |
    | `nltk` / `spaCy` | NLP tasks like tokenization and named entity recognition |
    | `jupyter`        | Interactive notebooks for exploration      
    ```
- After installing all required Python libraries, the project dependenciesw ere frozen into a requirements.txt file using `pip freeze > requirements.txt`. This records the exact versions of all installed packages, allowing anyone who clones the repository to recreate the same development environment using `pip install -r requirements.txt`. This ensures consistency, reproducibility, and easier collaboration across different systems.
- We added the initail basic info into the readme which we will expand as the project grows.
- Now that the structure is complete we will now give our first commit and push it to git hub.
- In order to make this project properly developed, we created a directory called as 'src' where we will store all the python code rather than placing the scripts in th root. So we moved the previously created the code directories into src directory.
    ```text
    TechPulse/
    │
    ├── src/
    │   ├── scrapers/
    │   ├── etl/
    │   ├── analysis/
    │   └── utils/
    ```


### Phase II - System Design

- Before writing the a single scraper, we're going to answer an important question:

> **How will data flow through our system?**

- Therefore, we defined a data pipeline:
```text
News Websites
      │
      ▼
Web Scraper
      │
      ▼
Raw Data (JSON)
      │
      ▼
ETL Pipeline
      │
      ▼
MySQL Database
      │
      ▼
SQL Analysis
      │
      ▼
Python Analysis & NLP
      │
      ▼
Tableau Dashboard
```
    - We do this so that each component has one responsibility:
    ```text
    | Component | Responsibility      |
    | --------- | ------------------- |
    | Scraper   | Collect data        |
    | ETL       | Clean and transform |
    | Database  | Store data          |
    | SQL       | Query and aggregate |
    | Python    | Advanced analysis   |
    | Tableau   | Visualize           |
    ```
    - This follows a **single responsibility principle**.

- We decided the data sources next. We will be using a hypbrid approach
    - Steps:
    1. Collect the latest article links from RSS feeds (wherever available).
    2. Visit Each article page and scrape the detailed information.

    - The initial 4 sources that we decided are 
    ```text
    | Source       | Why we chose it                 |
    | ------------ | ------------------------------- |
    | TechCrunch   | Startups, AI, funding, big tech |
    | The Verge    | Consumer technology and gadgets |
    | Ars Technica | Deep technical articles         |
    | VentureBeat  | AI, enterprise tech, startups   |

    These sources cover different areas of technology, which will make your analyses more interesting.
    ```
- One more thing which is important is to define a comman schema for all the sources so that even if they have different formats the data that we will save in the database will have consistency.
- For every source the pipeline will look like:
    ```text
    RSS Feed
        ↓
    Get article links
        ↓
    Visit article page
        ↓
    Extract data
        ↓
    Convert to common schema
        ↓
    Save as JSON
        ↓
    Run ETL
        ↓
    Store in MySQL
    ```
- **MY FIRST SOFTWARE ENGINEERING LESSON: ( Atlesdt, Thats what he said )**
    - A beginner always thinks: 
        > 'I'm building a scraper.'
    - An experienced developer thinks:
        > 'I'm Building a **frameword** that can support many scrappers.'
    
- Now we will design the **MySQL database from scratch**. We will identify all the entities, normalize the schema and create an ERD.
- Before creating the database we must first answer the questions :
> "What information does the business need to store ?"
> "What table are required to be created ?"

- To acheive a nice database we will proceed in following steps:
1. Understand the Business:
    > 'What information do we need ?'
    > 'What are the **things** in this system ?'
2. Identify entities:
    - An entity is something about which we want to store the information.
    Ex:
    ```
    Article

    Author

    Source

    Category

    Tag

    Company

    Technology
    ```
3. Determine Relationships: How are these entities connected ?
    1. Source --> articles ( 1 - many )
    2. Author --> articles ( 1 - many )
    3. Category --> articles ( 1 - many )
    4. Article --> Tags ( Many - Many ) --> We solve this using the bridge table
    5. Article --> Company ( Many - Many ) --> Bridge table.
    6. Article --> Technology ( Many - Many ) --> Bridge Table.
4. Think about future requirements: 
    - We should think in following manner:
    1. Tomorrow if we add another source into our list, will the database handle it ? Yes, because we are creating a seperate source table.
    2. Tomorrow if an article has 5 authors, will we support it ? yes , if we design carefully.
    3. If tomorrow we scrape 50 websites, our database will still withstand.
    4. If we scrape 100,000 articles/day, our database will still hold on.
    5. Define the tables that we will need.
    - Eventually our database will look like this -->
    ```
    techpulse

    │

    ├── articles ( Core )

    ├── authors ( Core )

    ├── sources ( Core )

    ├── categories ( Core )

    ├── companies ( Lookup )

    ├── technologies ( Lookup )

    ├── tags ( Lookup )

    ├── article_tags ( Bridge )

    ├── article_companies ( Bridge )

    ├── article_technologies ( Bridge )

    └── scrape_logs ( Operational )
    ```
- Now we will design the ERD. 

![Project Architecture](docs/images/techpulse_ERD.png)

- We can add two more tables to the database for better debugging. The two tables are --> 
1. scrape_jobs --> To understand where the job failed.
2. article_metrics --> For attributes like sentiment score, readability score etc.

### Phase III - Database Architect Design.

- We will proceed in steps from here:
1. I created two sql scripts.
    1. 01_create_database.sql
    2. 02_create_tables.sql

> "What is the heart of our system ?" --> **Articles**

- Articles table become our **fact table**.

- In first file we write the code :
```sql
CREATE DATABASE techpulse;

USE techpulse;
```

- Now i gave the second commit of the project. Creation of the database.

2.  We must decide the Data Architecture at this point. We ask :
> 'Where does every peice of data belong ?'.
- Now for this instead of thinking in tables we will think this in layers:
    1. Bronze Layer :
    - This layer contains the content exactly as we scraped it.
    - Even if there are any inconsistencies in the data.
    2. Silver Layer :
    - This layer will contain the clean and standardized data.
    - This is what most analysts will use.
    3. Gold Layer :
    - This layer stores business-ready analytics.
    1. Daily Article Counts
    2. Company mention Counts
    3. Technology trends etc....
    - This is optimized for dashboards and reporting only.
3. If we map tables according to the layer method we have:
    1. Bronze Layer :
    - bronze_articles
    - bronze_scrape_logs

    2. Silver Layer :
    - articles
    - article_versions
    - authors
    - sources
    - categories
    - companies
    - technologies
    - tags

    - article_authors
    - article_companies
    - article_technologies
    - article_tags

    3. Gold Layer :
    - daily_article_metrics
    - company_trends
    - technology_trends
    - source_metrics
    - category_metrics

4. Define the ETL Flow :
    Website

      ↓

    Bronze

      ↓

    Cleaning

      ↓

    Silver

      ↓

    Aggregation

      ↓

    Gold

      ↓

    Tableau

5. Create the ERD:
- This is already created above.
![Project Architecture](docs/images/techpulse_ERD.png)

6. Creation of necessary documents:
- We created the docs and named in numerical order. This demonstrated the procedure:
    1. 01_business_requirements.md --> Defines the database architecture, schema, relationships, and data flow for TechPulse.
    2. 02_system_architecture.md --> Defines TechPulse's system architecture, data flow, components, and technology stack.
    3. 03_database_design_specification.md -->  Defines the TechPulse database architecture, schema, relationships, and design principles.

### Phase IV - Database implementation.

#### Section I - Creation of Database Tables:

- Our database is already created.
- Now we will create our tables. We will proceed in dependency order so that foreign keys and all should not face any problem.
- Creation:
1. Table: sources
    - The sources table stores the data about every news publisher from which Techpulse collects articles.
    - Instead of repeating publisher information in every article we normalize it into a dedicated table.
    - This helps us in adding new sources etc.,.

    - For each source we ask the questions:
    1. What is its name ?
    2. What is the website ?
    3. What RSS feed does it expose ?
    4. What language does it publish in ?
    5. Which country is it based on ?
    6. Is scraping currently possible or enabled ?
    - Schema:
    ```sql
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
    ```
2. Table: categories
    - The categories table stores list of standardized news categories used throughout the platform.
    - It ensures consistent naming, Easier Filtering and No duplicate entries.
    - Schema:
    ```sql
    -- Categories Table: It stores the list of standardized news categories used throughout the platform.

    CREATE TABLE categories (
        category_id INT PRIMARY KEY AUTO_INCREMENT,
        category_name VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    ```
3. Table: authors
    - This is a difficult table as it required many to many relationship between authors and articles.
    - Schema:
    ```sql
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
    ```

4. Table: companies
    - Schema:
    ```sql
    -- Companies table: This table stores the list of organisations mentioned in the article

    CREATE TABLE companies (
        company_id INT PRIMARY KEY AUTO_INCREMENT,
        company_name VARCHAR(150),
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    ```
5. Table: technologies
    - Schema:
    ```sql
    -- Technologies table: This table stores the information about the technologies mentioned in the article

    CREATE TABLE technologies (
        technology_id INT PRIMARY KEY AUTO_INCREMENT,
        technology_name VARCHAR(100),
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    ```
6. Table: tags
    - Schema:
    ```sql
    -- Tags table: This table will store the topics as tags for proper filtering og the articles

    CREATE TABLE tags (
        tag_id INT PRIMARY KEY AUTO_INCREMENT,
        tag_name VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    ```
7. Table: **articles**
    - This is the most important and most complex table of this database so far.
    ```sql
    CREATE TABLE articles (
    article_id INT PRIMARY KEY AUTO_INCREMENT,
    article_url VARCHAR(1000) NOT NULL UNIQUE,
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
    ```
8. Now we will design the bridge tables for our many - many relationship.
    1. Table: article-authors:
        ```sql
        CREATE TABLE articles (
        article_id INT PRIMARY KEY AUTO_INCREMENT,
        article_url VARCHAR(1000) NOT NULL UNIQUE,
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
        ```

    2. Table: article_companies
        ```sql
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
        ```

    3. Table: article_technologies
        ```sql
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
        ```

    4. Table: article_tags
        ```sql
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
        ```

9. Final Table: scrape_logs
    ```sql
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
    ```

#### Section II - Creation Of Indexes

- We created the indexes using the code:
```sql
-- Articles
CREATE INDEX idx_articles_source
ON articles(source_id);

CREATE INDEX idx_articles_category
ON articles(category_id);

CREATE INDEX idx_articles_published_at
ON articles(published_at);

-- Authors
CREATE INDEX idx_authors_source
ON authors(source_id);

-- Scrape Logs
CREATE INDEX idx_scrape_logs_source
ON scrape_logs(source_id);

CREATE INDEX idx_scrape_logs_status
ON scrape_logs(status);
```

#### Section III - Creation of Views:

```sql
-- Creating the Views


-- 1. Article Details
CREATE VIEW vw_article_details AS
SELECT
    a.article_id,
    a.title,
    a.summary,
    a.article_url,
    s.source_name,
    c.category_name,
    a.published_at,
    a.scraped_at,
    a.word_count,
    a.reading_time
FROM articles a
JOIN sources s
    ON a.source_id = s.source_id
JOIN categories c
    ON a.category_id = c.category_id;


-- 2. Company Mentions
CREATE VIEW vw_article_details AS
SELECT
    a.article_id,
    a.title,
    a.summary,
    a.article_url,
    s.source_name,
    c.category_name,
    a.published_at,
    a.scraped_at,
    a.word_count,
    a.reading_time
FROM articles a
JOIN sources s
    ON a.source_id = s.source_id
JOIN categories c
    ON a.category_id = c.category_id;
    
-- Technology Mentions
CREATE VIEW vw_technology_mentions AS
SELECT
    a.article_id,
    a.title,
    t.technology_name,
    s.source_name,
    a.published_at
FROM article_technologies at
JOIN articles a
    ON at.article_id = a.article_id
JOIN technologies t
    ON at.technology_id = t.technology_id
JOIN sources s
    ON a.source_id = s.source_id;


-- Author Details
CREATE VIEW vw_article_authors AS
SELECT
    a.article_id,
    a.title,
    au.display_name,
    s.source_name,
    a.published_at
FROM article_authors aa
JOIN articles a
    ON aa.article_id = a.article_id
JOIN authors au
    ON aa.author_id = au.author_id
JOIN sources s
    ON a.source_id = s.source_id;
    
    
-- Tag Details
CREATE VIEW vw_article_tags AS
SELECT
    a.article_id,
    a.title,
    t.tag_name,
    s.source_name,
    a.published_at
FROM article_tags at
JOIN articles a
    ON at.article_id = a.article_id
JOIN tags t
    ON at.tag_id = t.tag_id
JOIN sources s
    ON a.source_id = s.source_id;
    

-- Scraping Activity
CREATE VIEW vw_scrape_summary AS
SELECT
    sl.log_id,
    s.source_name,
    sl.scrape_started_at,
    sl.scrape_completed_at,
    sl.articles_found,
    sl.articles_inserted,
    sl.status
FROM scrape_logs sl
JOIN sources s
    ON sl.source_id = s.source_id;
```

#### Section IV : Creating Seed Data.

```sql


-- Seed Data

-- Sources Table
INSERT INTO sources (
    source_name,
    website_url,
    rss_feed_url,
    country,
    language
)
VALUES
('TechCrunch','https://techcrunch.com','https://techcrunch.com/feed/','USA','en'),

('The Verge','https://www.theverge.com','https://www.theverge.com/rss/index.xml','USA','en'),

('Ars Technica','https://arstechnica.com','https://feeds.arstechnica.com/arstechnica/index','USA','en'),

('VentureBeat','https://venturebeat.com','https://venturebeat.com/feed/','USA','en');


-- Categories Table

INSERT INTO categories (category_name)
VALUES
('Artificial Intelligence'),
('Cloud Computing'),
('Cybersecurity'),
('Programming'),
('Robotics'),
('Startups'),
('Consumer Technology'),
('Data Science');

-- Technologies Table
INSERT INTO technologies (technology_name)
VALUES
('Python'),
('Docker'),
('Kubernetes'),
('TensorFlow'),
('PyTorch'),
('CUDA'),
('MySQL'),
('PostgreSQL'),
('React'),
('Node.js'),
('LangChain'),
('Apache Spark');


-- Tags
INSERT INTO technologies (technology_name)
VALUES
('Python'),
('Docker'),
('Kubernetes'),
('TensorFlow'),
('PyTorch'),
('CUDA'),
('MySQL'),
('PostgreSQL'),
('React'),
('Node.js'),
('LangChain'),
('Apache Spark');


-- Companies 
INSERT INTO companies (company_name)
VALUES
('OpenAI'),
('Microsoft'),
('Google'),
('Meta'),
('Apple'),
('Amazon'),
('NVIDIA'),
('Anthropic'),
('Tesla');
```

#### Section V : Validation and Testing
```sql


-- Validation and Testing

SHOW TABLES;

DESCRIBE articles;
DESCRIBE article_authors;
DESCRIBE article_tags;
DESCRIBE article_technologies;
DESCRIBE categories;
DESCRIBE companies;
DESCRIBE scrape_logs;
DESCRIBE sources;
DESCRIBE tags;
DESCRIBE technologies;
DESCRIBE vw_article_details;
DESCRIBE vw_scrape_summary;
DESCRIBE vw_technology_mentions;

SHOW INDEX FROM articles;
SHOW INDEX FROM sources;
SHOW INDEX FROM authors;
SHOW INDEX FROM scrape_logs;

SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA='techpulse'
AND REFERENCED_TABLE_NAME IS NOT NULL;

INSERT INTO articles
(
article_url,
source_id,
category_id,
title,
summary,
content,
published_at,
word_count,
reading_time,
content_hash
)
VALUES
(
'https://example.com/article1',
1,
1,
'OpenAI launches GPT-6',
'Summary',
'Content...',
NOW(),
800,
4,
SHA2('Content...',256)
);

SELECT * FROM articles LIMIT 10;

SELECT * FROM vw_article_details;
```


### Phase V - Web Scraper Development.

- Created the directory structure as:
```text
TECHPULSE
│
├── config
│
├── data
│   ├── raw
│   ├── processed
│   └── exports
│
├── database
│
├── dashboard
│
├── docs
│
├── logs
│
├── notebooks
│
├── reports
│
├── src
│   │
│   ├── analysis
│   │
│   ├── etl
│   │
│   ├── scrapers
│   │   │
│   │   ├── common
│   │   │   ├── base_scraper.py
│   │   │   ├── rss_scraper.py
│   │   │   ├── html_parser.py
│   │   │   ├── database.py
│   │   │   ├── logger.py
│   │   │   └── helpers.py
│   │   │
│   │   ├── sources
│   │   │   ├── techcrunch.py
│   │   │   ├── theverge.py
│   │   │   ├── venturebeat.py
│   │   │   └── arstechnica.py
│   │   │
│   │   └── scraper_runner.py
│   │
│   └── tests
│
├── implementation.md
├── main.py
├── README.md
├── requirements.txt
└── LICENSE
```

- We created a article.py file which holds the article class to store the scraped data in a particular order. This is helpful when we scrape data from different sources and the data is scraped in different formats that usual.
- Every scraper should follow the same pipeline :
    ```text
    Website
        │
        ▼
    Download HTML
        │
        ▼
    Extract Information
        │
        ▼
    Create Article Object
        │
        ▼
    Return Article
        │
        ▼
    Database Loader
    ```

- The framework which we will use is this:
    ```text
                        Scraper Runner
                            │
            ┌───────────────┼───────────────┐
            ▼                               ▼
        TechCrunch Scraper             The Verge Scraper
            │                               │
            └───────────────┬───────────────┘
                            ▼
                    Base Scraper
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
        HTTP Client     RSS Parser     HTML Parser
    ```
- Now, We will build a Base Scraper:
    - We create src/scraper/common/base_scraper.py
    - We use the code as below and i will explain everything in proper understanding:
    ```python
    import logging  # Use to print log messages
    import time  # Used for keeping the scraper on hold before it retries
    from abc import ABC # Abstract Base Class : Intend to be a parent Class
    from typing import Optional # This is for times when something is not present

    import requests # This is for requesting information from the websites
    from requests import Response # This is used to store the recieved response
    ```

    ```python
    class BaseScraper(ABC):
    def __init__(self, timeout: int = 15, retries: int = 3, delay: int = 2):
        self.timeout = timeout
        self.retries = retries
        self.delay = delay
    ```
    - We defined a BaseScraper class on which the other scrapers will be built on.
    - The constructor function takes in 3 parameters.

    ```python
    self.headers = {
            'User-Agent': (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )
        }
    ```
    - This is used so that website doesnt think that we are using a scraper. It must rather think that we are requesting from a browser.

    `self.logger = logging.getLogger(self.__class__.__name__)`
    - This line used to print the current class's name in the log.

    `def fetch(self, url: str) -> Optional[Response]:`
    - We are defining the fetch function on which will request the website to issue the data. There can be a no response situation so we are using the OPTIONAL response technique.

    ```python
    for attempt in range(1, self.retries + 1):

            try:

                response = requests.get(url, headers=self.headers, timeout=self.timeout)

                response.raise_for_status()

                return response

            except requests.RequestException as e:

                self.logger.warning(
                    f"Attempt {attempt} failed: {e}"
                )

                if attempt < self.retries:
                    time.sleep(self.delay)
    ```
    - We are using a for loop for 3 times so that we make 3 attempts to fetch the data.
    - 'raise_for_status' this is used for the cases when the response is like and error which is like 404 or 500. This raises an exception at that moment.
    - If everything is working, return the fetched response.
    - For exceptions we are raising a warning in the logs.
    - Then after the request is done we are checking if the attempt is less than the retries. If yes we are adding a delay of 3 seconds.

    ```python
        self.logger.error(f"Failed to fetch {url}")

        return None
    ```

    - When all the attempts are completed and we still got nothing. Then we return nothing with an error in the log.

    - We are building this to write efficient code. Rather than writing the code for seperate scrapers seperately, we just use this BaseScraper Class.

- Now we will build, RSS Scraper:
    ```python
    import logging
    from typing import List, Dict

    import feedparser
    ```
    - Logging for logger and typing to convert the recieved data into List of dictionaries and feedparser is used to parse the XML based RSS feeds in easy to use python objects.
    
    ```python
    class RSSScraper:
    def __init__(self):
        self.logger = logging.getLogger(
            self.__class__.__name__
        )
    ```
    - We created the RSSScraper class which will be used as a blueprint for different RSS feed sources.

    ```python
    def parse_feed(self, rss_url : str) -> List[Dict]:
        feed = feedparser.parse(rss_url)

        articles = []

        if feed.bozo:

            self.logger.warning(
                "RSS Feed contains parsing error."
            )

        for entry in feed.entries:

            articles.append({
                "title": entry.get("title"),

                "url": entry.get("link"),

                "published": entry.get('published'),

                "summary": entry.get('summary')
            })

        return articles
    ```
    - We define a function used to get and parse the feed from RSS. We created an empty list in which we will store the articles. This list will be holding dictionaries. 
    - 'feed' object will hold all the articles as entries from the response. 
    - Then for each feed we take the necessary elements and store it in 'articles' list.
    - Now all the sources that we will use for RSS scraper will be done using this class.
    ```python
    rss = RSSScraper()

    articles = rss.parse_feed(
        "https://techcrunch.com/feed/"
    )

    print(len(articles))

    print(articles[0])
    ```
    - We are not creating a dataclass just yet as we dont have enough information to build our Article Dataclass. This information just says "Here is something, here is where to find it."
    - We will use the html parser to get the actual article data from each html page.

#### Plan had some changes.

- We have removed the sources folder. And created seperate packages for different sources. As they will have different formats we will use different scrapers for each of the source. Those scrapers will be built on top of **baseScraper class**. The rss.py will fetch the list of articles and return us the details for each article including the urls. Then we will use the scrapers to fetch each url's html and then parse to and append it into a list. Then we will use the scraper_runner.py file to accumulate all the data from different sources into one place.

- Now we will change the rss.py code:
    ```python
    import logging
    from typing import List

    import feedparser

    logger = logging.getLogger(__name__)

    def get_article_urls(rss_url: str) -> List[str]:
        
        feed = feedparser.parse(rss_url)

        if feed.bozo:
            logger.warning(
                "RSS feed contains parsing errors: %s",
                getattr(feed, "bozo_exception", "Unknown error")
            )

        article_urls = []
        seen_urls = []

        for entry in feed.entries:
            url = entry.get("link")

            if not url:
                continue

            if url in seen_urls:
                continue

            seen_urls.add(url)
            article_urls.append(url)

        logger.info(
            "Discovered %d articles URLs from RSS feed.", 
            len(article_urls)
        )

        return article_urls
    ```

- Later we will use it like :
```python
from scrapers.common.rss import get_article_urls

rss_url = "https://techcrunch.com/feed/"

article_urls = get_article_urls(rss_url)

for url in article_urls:
    # Download HTML
    # Pass HTML to parser
    # Create Article object
    pass
```

- Now we will create our first scrapper.
    - Before we begin writing the code, we will take a live TechCrunch article and understand the exact HTML selectors for each field.
    - We created a common python file called as article_enricher.py which is responsible for deriving information that does not exist in the HTML. This module take the parsed article object and enrich it with calculated fields before it is stored in the database.
    - All of the helper functions are in the helpers.py file which are used by the article_enricher.py file.
    - Final Pipeline as of now Looks like this :
    ```python
    RSS Feed
      │
      ▼
    get_article_urls()
        │
        ▼
    TechCrunchScraper
        │
        ▼
    Download HTML
        │
        ▼
    TechCrunchParser
        │
        ▼
    Article
        │
        ▼
    ArticleEnricher
        │
        ▼
    DatabaseLoader
        │
        ▼
    MySQL
    ```

- Writing helpers.py functions: So that every future scraper will benefit from it. Basically `helpers.py` is a library of pure utility functions in which each function take an input, return an output and have no side effects. 
- Initially we will implement only 5 functions:
1. clean text
2. calculate word count
3. calculate reading time
4. generate_content_hash
5. parse_datetime
- `helpers.py` file will have the code:
```python
import hashlib
import math
import re
from datetime import datetime
from typing import Optional


def clean_text(text: Optional[str]) -> str:
    """
    Clean and normalize text by removing extra whitespace.

    Args:
        text: Input text.

    Returns:
        Cleaned text.
    """
    if not text:
        return ""

    # Replace multiple whitespace characters with a single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def calculate_word_count(text: str) -> int:
    """
    Calculate the number of words in a text.

    Args:
        text: Input text.

    Returns:
        Word count.
    """
    if not text:
        return 0

    return len(text.split())


def calculate_reading_time(
    word_count: int,
    words_per_minute: int = 200
) -> int:
    """
    Estimate reading time in minutes.

    Args:
        word_count: Total number of words.
        words_per_minute: Average reading speed.

    Returns:
        Estimated reading time in minutes.
    """
    if word_count <= 0:
        return 0

    return math.ceil(word_count / words_per_minute)


def generate_content_hash(text: str) -> str:
    """
    Generate a SHA-256 hash for article content.

    Args:
        text: Article content.

    Returns:
        SHA-256 hash string.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_datetime(datetime_str: Optional[str]) -> Optional[datetime]:
    """
    Parse an ISO-8601 datetime string into a datetime object.

    Args:
        datetime_str: Datetime string.

    Returns:
        datetime object if parsing succeeds, otherwise None.
    """
    if not datetime_str:
        return None

    try:
        return datetime.fromisoformat(datetime_str)
    except ValueError:
        return None
```

- To use this functions we will create the article_enrichers for derived content as code:
```python
from .article import Article
from .helpers import (
    clean_text,
    calculate_reading_time,
    calculate_word_count,
    generate_content_hash
)


class ArticleEnricher:
    '''
    Enriches an Article Object by calculating derived field.

    Responsibilities:
        - Clean Article text
        - Calculate word count
        - Estimate reading time
        - Generate content hash
    '''

    def enrich(self, article: Article) -> Article:
        '''
        Enriches an article with calculated metadata.

        Args:
            article: Parsed Article Object.

        Returns:
            Enriched Article Object.
        '''

        # Calculate derived fields
        article.word_count = calculate_word_count(article.content)

        article.reading_time = calculate_reading_time(
            article.word_count
        )

        article.content_hash = generate_content_hash(
            article.content
        )

        return article
```
- This takes the article as input add the derived fields using the helper functions and return the modified article in universal format.

#### Implementation of first END to END pipeline of data scraping.

```text
RSS Feed
    │
    ▼
get_article_urls()
    │
    ▼
TechCrunchScraper
    │
    ▼
Download HTML
    │
    ▼
TechCrunchParser
    │
    ▼
Article
    │
    ▼
ArticleEnricher
    │
    ▼
Database Loader
```

- Creating the techcrunch/parser.py
    - The responsibility is just to convert the TechCrunch HTML page into an Article Object. That's it.
    - Tehe parser also uses the helper fuctions from the helpers.py to add some derived fields as well into the article as we require in the database.

- We now create the scraper for techcruch which will use the baseScraper as its parent class.
- The implementation looks like this:
    ```python
    from bs4 import BeautifulSoup

    from scrapers.common.article import Article
    from scrapers.common.article_enricher import ArticleEnricher
    from scrapers.common.base_scraper import BaseScraper
    from scrapers.common.rss import get_article_urls

    from .parser import TechCrunchParser

    ```
    - These are all the things that we created before this and we will use these in the scraper.

    ```python
    class TechCrunchScraper(BaseScraper):
    """
    Scraper responsible for collecting and parsing
    TechCrunch articles.
    """

    RSS_URL = "https://techcrunch.com/feed/"

    def __init__(self):
        super().__init__()

        self.parser = TechCrunchParser()
        self.enricher = ArticleEnricher()
    ```
    - We are creating the class for TechCrunchScraper which take the BaseScraper as its parent class.
    - We have hard coded the RSS_URL because there is no need of dynamics.
    
    ```python
       def scrape(self) -> list[Article]:
        """
        Scrape all articles from the TechCrunch RSS feed.

        Returns:
            List of enriched Article objects.
        """

        articles = []

        article_urls = get_article_urls(self.RSS_URL)

        self.logger.info(
            "Found %d article URLs.",
            len(article_urls)
        )

        for url in article_urls:

            response = self.fetch(url)

            if response is None:
                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            try:

                article = self.parser.parse(
                    soup=soup,
                    article_url=url
                )

                article = self.enricher.enrich(article)

                articles.append(article)

            except Exception as e:

                self.logger.exception(
                    "Failed to parse article %s : %s",
                    url,
                    e
                )
    ```
    - We are first getting the list of articles using the get_article_urls.
    - Then we add a logging statement
    - Then for each url in the list of article_urls found we will fetch the html using fetch method.
    - If response is not there we just continue and then we are converting the html into a BeautifulSoup object which the parser understands.
    - Then we are parsing that BeautifulSoup Object using our parser for techcrunch
    - After parsing it we are enriching using our enricher. 
    
    ```python
    self.logger.info("Successfully scraped %d articles.", len(articles))

        return articles
    ```
    - Upon successful completion of the code we return the articles list.
    - This is our Scraper.
- The workflow looks like this:
```text
RSS Utility
      │
      ▼
Discovers article URLs
      │
      ▼
BaseScraper
      │
      ▼
Downloads HTML
      │
      ▼
BeautifulSoup
      │
      ▼
TechCrunchParser
      │
      ▼
Creates Article
      │
      ▼
ArticleEnricher
      │
      ▼
Adds derived fields
      │
      ▼
List[Article]
```

- **Each component in our setup has exactly one job in the entire process.**

- Before implementing the database.py we will first test it using a small script.
- The test file was written as:
```python


from scrapers.techcrunch.scraper import TechCrunchScraper

def main():
    scraper = TechCrunchScraper()

    articles = scraper.scrape()

    if len(articles) <=0:
        print("No articles scraped.")

    print(f"Successfully scraped {len(articles)} articles. \n")

    if articles:
        article = articles[0]

        print("=" * 80)
        print(f"Title          : {article.title}")
        print(f"Author(s)      : {article.authors}")
        print(f"Category       : {article.category}")
        print(f"Published At   : {article.published_at}")
        print(f"Word Count     : {article.word_count}")
        print(f"Reading Time   : {article.reading_time} min")
        print(f"Tags           : {article.tags}")
        print(f"Content Hash   : {article.content_hash}")
        print("\nSummary:")
        print(article.summary)
        print("\nContent Preview:")
        print(article.content[:500])
        print("=" * 80)


if __name__ == '__main__':
    main()
```
and the above code when run in the root folder of the project in terminal if returns:
```text
zama@LAPTOP-QF0LKB3O MINGW64 ~/Desktop/Techpulse (main)
$ python -m tests.test_techcrunch_scraper
2026-07-03 11:43:57,103 | INFO | TechCrunchScraper | Found 20 article urls
2026-07-03 11:44:01,072 | INFO | TechCrunchScraper | Successfully scraped 20 articles.
Successfully scraped 20 articles. 

================================================================================
Title          : Politician who investigated spyware abuses had his phone hacked with Pegasus spyware
Author(s)      : ['Zack Whittaker']
Category       : Security
Published At   : 2026-07-02 22:05:00-07:00
Word Count     : 0
Reading Time   : 0 min
Tags           : ['cybersecurity', 'Government & Policy', 'NSO Group', 'Pegasus', 'Security', 'Spyware']
Content Hash   : e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Summary:
Security researchers have confirmed that a European politician had his phone hacked with the Pegasus spyware while serving on an investigatory committee probing abuses of the notorious surveillance tool. This has reigniting fresh controversy over governments abusing spyware to collect information about their critics.

Content Preview:

================================================================================
(.venv) 
mzama@LAPTOP-QF0LKB3O MINGW64 ~/Desktop/Techpulse (main)
$ 
```
- This means our pipeline is running just fine. But there is an issue in the words_count and read_time. That shows us that the parser is not able to extract the content. That is why the _extract_content is returning none.
- With little bit of debugging from the terminal we are found to be successful
```text
mzama@LAPTOP-QF0LKB3O MINGW64 ~/Desktop/Techpulse (main)
$ python -m tests.test_techcrunch_scraper
2026-07-03 12:04:52,909 | INFO | TechCrunchScraper | Found 20 article urls
2026-07-03 12:04:56,784 | INFO | TechCrunchScraper | Successfully scraped 20 articles.
Successfully scraped 20 articles. 

================================================================================
Title          : Politician who investigated spyware abuses had his phone hacked with Pegasus spyware
Author(s)      : ['Zack Whittaker']
Category       : Security
Published At   : 2026-07-02 22:05:00-07:00
Word Count     : 776
Reading Time   : 4 min
Tags           : ['cybersecurity', 'Government & Policy', 'NSO Group', 'Pegasus', 'Security', 'Spyware']
Content Hash   : f28175d80816bf78a3d8395a5d5739f3901f7dcb1e8c08fa9a9898d8c8271ae9

Summary:
Security researchers have confirmed that a European politician had his phone hacked with the Pegasus spyware while serving on an investigatory committee probing abuses of the notorious surveillance tool. This has reigniting fresh controversy over governments abusing spyware to collect information about their critics.

Content Preview:
Security researchers have confirmed that a European politician had his phone hacked with the Pegasus spyware while serving on an investigatory committee probing abuses of the notorious surveillance tool. This has reigniting fresh controversy over governments abusing spyware to collect information about their critics.

The researchers at the University of Toronto’s digital rights unit The Citizen Lab say the confirmed phone hacking of Greek journalist and former politician Stelios Kouloglou durin
================================================================================
(.venv) 
mzama@LAPTOP-QF0LKB3O MINGW64 ~/Desktop/Techpulse (main)
$ 
```
- Raw article looks like this:
```
Article(article_url='https://techcrunch.com/2026/07/07/savis-app-aims-to-protect-consumers-from-realistic-ai-scams-like-kidnappers-demanding-ransom/', source_name='TechCrunch', title='Savi’s app aims to protect consumers from realistic AI scams like kidnappers demanding ransom', summary='Brothers Patrick and Ryan Coughlin, each with impressive careers in the tech industry (Patrick worked in national cyber defense, and at Splunk and Cisco; and Ryan with consumer products at Apple and Spotify), have launched a new kind of security startup.', content='Brothers Patrick and Ryan Coughlin, each with impressive careers in the tech industry (Patrick worked in national cyber defense, and at Splunk and Cisco; and Ryan with consumer products at Apple and Spotify), have launched a new kind of security startup.\n\nSavi Security seeks to protect everyday folks from the new crop of incredibly convincing AI-generated scams, whether they’re routed via text, emails or phone calls.\n\nThe company just raised $7 million in seed funding, and is launching its app for iPhone and Android on Tuesday. The round was led by Acrew Capital, with participation from Magnify Ventures, TTCER, and Resolute Ventures.\n\nThe inspiration for the company came from a horrifying incident involving the founders’ mother.\n\nAbout two years ago, Patrick Coughlin’s mom called him, distraught, saying she had just received a phone call from a man saying he had kidnapped Coughlin’s sister. He was senior vice president of security products at Cisco at the time. (He landed there after Splunk bought his cloud security startup TruSTAR for a reported $82 million in May 2021. In 2024, Cisco bought Splunk.)\n\nHer mobile phone rang with the caller ID of her daughter, Coughlin recounted. During that call, “she thinks she hears my sister’s voice saying, ‘Mom, they’ve got me.’ There’s a blood-curdling scream, and then my sister says, ‘You’ve got to do what they tell you.’ And then a man comes on the phone and says, ‘If you don’t pay us $1,200 right now, we’re going to kill your daughter in the parking lot of the local Walmart,’” he continued.\n\nThe scammer had accurately spoofed Coughlin’s sister’s number, her voice, and referenced the location of the Walmart she frequented.\n\nFortunately, the mom kept her wits, called the daughter, and discovered that she was fine. The kidnapping was an AI-generated scam.\n\nCoughlin, like his mom, was shaken.\n\n“What I was thinking, after calming my mom down is: What has fundamentally changed in the underlying cybercriminal economy that we are now able to lever the same kind of sophistication that I had seen pointed at government agencies, and then later at Fortune 500 companies? And now we’re deploying that sophistication at the consumer?”\n\nThe answer is, of course, cheap and powerful LLMs and other generative AI tools.\n\nBefore AI, pursuing such grifts on consumers was not financially worth it. It would require in-depth research on the target, tech to spoof voices, and so on. Such attacks were primarily aimed only at deep pockets, like enterprises or governments, as was the tech to defend against them.\n\n“There’s something that’s happening right now to consumers with AI in the hands of cyber criminals,” Coughlin says. The costs to perpetrate such swindles have become negligible, and the research material, easily available.\n\n“You can clone a voice off three seconds of audio, off a publicly available social media post. So we’ve all got these traces of stuff that’s out there in the ether — like where we’re talking or narrating; commenting on a kid’s football game while videotaping it, and putting it on Facebook.”\n\nThe FTC said last month that people reporting online crimes collectively lost $3.5 billion to imposter scams in 2025, triple the amount in 2020. While the majority of people reporting such scams are older Americans, some research implies Gen Z is also highly susceptible. Research from 2025 by Malwarebytes, a maker of antivirus and anti-malware tools, reported that Gen Z was targeted more often with text scams than other generations, and fell for them about 25% of the time.\n\nThe Coughlin brothers’ idea was to develop a real-time intervention tool.\n\nThey tested their idea, and the AI scam detection model they were building, by launching a free website called Scam Wise . It is anonymous, no registration required. Just upload any suspicious texts, photos or emails, and Scam Wise will determine if it’s likely to be bogus.\n\n“We launched that about four months ago. We’ve had 50,000 submissions, and it grows now every week by about 10,000 submissions or more,” Coughlin said.\n\nScam Wise proved a source of in-the-wild data to help train Savi’s scam-detection AI model. The startup is currently mostly using Google’s Gemini, but has built its software on an AI gateway, which allows it to tap other AI models as needed, like voice detection-specific options.\n\nOn Tuesday, Savi launched a paid product, an iOS and Android app for consumers, that can screen texts, voicemails and incoming calls for scams.\n\nSuch features are available in a lot of different products (such as Malwarebytes), but Savi’s most impressive feature is live call monitoring.\n\nDuring a suspicious phone conversation, a user can opt to add the app’s live agent as a listener. Savi listens for behavioral tells that can identify if the situation is a grift while the call is in progress.\n\nSavi’s fees are also a bit unusual. It charges $8/month, discounted to $63/year, to cover an entire family, and puts no cap on the number of users. So one plan can cover a person’s kids, spouse, parents, and that uncle who always seems to need tech support. Or whoever else that the primary account holder wants to add and provide administrative support to.\n\nAI has changed the conditions for “how accessible being a fraudster is,” Coughlin said. “We’re creating fraudsters because we’re bringing down the barrier of deceiving people. So not only do we have the organized criminals and the syndicates behind this, but everyday people are sort of being tempted into playing fraud.”\n\nSavi Security’s answer is like a new generation of anti-virus-like software: one that uses AI in real time just like the bad guys do.', authors=['Julie Bort'], category='AI', tags=['AI', 'AI scams', 'fraud detection', 'Savi', 'Security', 'Startups'], companies=[], technologies=[], published_at=datetime.datetime(2026, 7, 7, 5, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))), word_count=937, reading_time=5, content_hash='632a3f3d2f2c423ea3f0e3f6c1d2dd0b2f8b8af76af8068165f62e395d8639ef', scraped_at=datetime.datetime(2026, 7, 7, 12, 21, 15, 99423))
```

- Now we will design the database loader which is database.py .
- We have created two files. .env for credentials of the database and .env_example for reference of how the contents of the database are.
- .env file is filled with
```python
from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DF_USER")
DF_PASSWORD = os.getenv("DB_PASSWORD")
```

- Now we created a settings.py in config folder:
```python
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
```

- Then we implemented the database connection file:
```python
import mysql.connector

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection and self.connection.is_connected():
            self.connection.close()

    def is_connected(self):
        return (
            self.connection is not None
            and self.connection.is_connected()
        )
```

- Then to test it we created tests/test_database_connection.py
```python
from src.common.database import Database


def main():
    db = Database()

    try:
        db.connect()

        print("Database connected successfully.")

        cursor = db.get_cursor()
        cursor.execute("SELECT 1")

        print(cursor.fetchone())

    finally:
        db.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
```

- Then we ran the file using the command `python -m tests.test_database_connection.py` and it returned the text as 
```text
mzama@LAPTOP-QF0LKB3O MINGW64 ~/Desktop/Techpulse (main)
$ python -m tests.test_database_connection
Database connected Successfully.
(1,)
Connection Closed.
(.venv) 
```

- Now we will create the **Database loader**.
    - The only responsibility of a database loader is to load a fetch article and load it into the relational database in MySQL and also it must load different relational entities into different tables along with relations.
    - The data flow looks like this:
    ```text
    Receive Article
        │
        ▼
    Article Exists?
        │
        ├── Yes → Return
        │
        ▼
    Get/Create Source
        │
        ▼
    Get/Create Category
        │
        ▼
    Get/Create Author(s)
        │
        ▼
    Insert Article    
        │
        ▼
    Get/Create Companies
        │
        ▼
    Insert Article Companies
        │
        ▼
    Get/Create Technologies
        │
        ▼
    Insert Article Technologies
        │
        ▼
    Get/Create Tags
        │
        ▼
    Insert Article Tags
        │
        ▼
    Insert Article Authors
        │
        ▼
    Commit
    ```

    - There must be only one API method which is:
    loader.load_articles(articles)
    - Now the internal methods will be like:
    ```text
    DatabaseLoader
    │
    ├── load_articles()
    │
    ├── _load_single_article()
    │
    ├── _article_exists()
    │
    │
    ├── _insert_article()
    │
    │
    ├── _get_or_create_source()
    ├── _get_or_create_author()
    ├── _get_or_create_category()
    ├── _get_or_create_company()
    ├── _get_or_create_technology()
    ├── _get_or_create_tag()
    │
    ├── _insert_article_authors()
    ├── _insert_article_companies()
    ├── _insert_article_technologies()
    ├── _insert_article_tags()
    │
    └── _get_or_create()
    ```
    - Each method has one single responsibility.
    - We will use all the hidden individual methods inside a master public method to get this done nicely.
    - Inside load articles: The flow is like:
    ```text
    for article in articles
        try
            _load_single_article
        except
            log error
    ```

    - Inside the _load_single_article, the flow will be like:
    ```text
    if _article_already_exists:
        return
    else:
        source_id
        author_id
        insert article
        insert categories
        insert companies
        insert technologies
        insert tags 
        commit
    ```

    - Inside the _insert_article method, it must only do:
    ```text
    recieve article, source_id, author_id and insert it into the articles table and return the article_id
    ```
    - Same thing happens in different insert methods. 
    - Instead of one bridge_table for all we must implement different bridge tables for all the realtionships as they have different set of parameters and different tables to look into. It is better for code readability

    - Transactions: Instead of commiting every step we must commit only once per article at the end of the process. This maintains the database consistency. If an error occurs midway we can rollback.
    - Code:
    ```python
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
    ```
    - This is tested using the code:
    ```python
    from src.scrapers.common.database_loader import DatabaseLoader
    from src.scrapers.common.database import Database

    from datetime import datetime, timezone, timedelta
    from src.scrapers.common.article import Article   # assuming you saved your dataclass in article_model.py


    def main():
        # Create Article dataclass object instead of dict
        article = Article(
            article_url="https://techcrunch.com/2026/07/07/savis-app-aims-to-protect-consumers-from-realistic-ai-scams-like-kidnappers-demanding-ransom/",
            source_name="TechCrunch",
            title="Savi’s app aims to protect consumers from realistic AI scams like kidnappers demanding ransom",
            summary="Brothers Patrick and Ryan Coughlin, each with impressive careers in the tech industry...",
            content="Full article content here...",
            authors=["Julie Bort"],
            category="AI",
            tags=["AI", "AI scams", "fraud detection", "Savi", "Security", "Startups"],
            companies=[],
            technologies=[],
            published_at=datetime(2026, 7, 7, 5, 0, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            word_count=937,
            reading_time=5,
            content_hash="632a3f3d2f2c423ea3f0e3f6c1d2dd0b2f8b8af76af8068165f62e395d8639ef",
            scraped_at=datetime(2026, 7, 7, 12, 21, 15, 99423)
        )

        SOURCE_METADETA = {
            "source_name": "TechCrunch",
            "website_url": "https://techcrunch.com",
            "rss_feed_url": "https://techcrunch.com/feed/",
            "country": None,
            "language": "en"
        }

        db = Database()
        db.connect()
        loader = DatabaseLoader(db)

        try:
            hey = loader.load_articles([article], SOURCE_METADETA)
            print(hey)
        except Exception as e:
            print("Error:", e)


    if __name__ == "__main__":
        main()
    ```
- We have completed the logging for all the previously created files.

- Now we implement the pipeline integrator. At this moment we have two different processes. 
1. scrape and parse.
2. Database loader to MYSQL
- We need to connect these two now. That is done using a integrator.
- Code for the integrator is as follows:
```python
from scrapers.common.database import Database
from scrapers.common.database_loader import DatabaseLoader
from scrapers.common.logger import get_logger
from scrapers.techcrunch.scraper import TechCrunchScraper

logger = get_logger("TechCrunch Integrator")


class TechCrunchIntegrator:
    """
    Orchestrates the complete TechCrunch ETL pipeline.

    Pipeline:
    1. Scrape articles from TechCrunch.
    2. Load the scraped articles into the database.
    """

    def run(self):

        logger.info("Starting TechCrunch integration pipeline.")

        scraper = TechCrunchScraper()

        logger.info("Scraping articles from TechCrunch.")
        articles = scraper.scrape()

        db = Database()
        db.connect()

        try:
            logger.info("Loading scraped articles into the database.")

            loader = DatabaseLoader(db)
            loader.load_articles(articles, scraper.SOURCE_METADATA)

            logger.info(
                "TechCrunch integration pipeline completed successfully."
            )

        except Exception:
            logger.exception("TechCrunch integration pipeline failed.")
            raise

        finally:
            logger.info("Closing database connection.")
            db.close()
```
