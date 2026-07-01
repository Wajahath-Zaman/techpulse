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

