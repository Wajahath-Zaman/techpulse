
USE techpulse;

-- In this file we will be creating views for our analytics

-- 1. The master table

CREATE OR REPLACE VIEW vw_article_master AS
SELECT
    a.article_id,
    a.title,
    a.summary,
    a.article_url,

    s.source_name,
    s.country,
    s.language,

    c.category_name,

    a.published_at,
    DATE(a.published_at) AS published_date,

    YEAR(a.published_at) AS published_year,
    MONTH(a.published_at) AS published_month,
    MONTHNAME(a.published_at) AS month_name,
    QUARTER(a.published_at) AS quarter,
    WEEK(a.published_at) AS week_number,
    DAYNAME(a.published_at) AS weekday,

    a.word_count,
    a.reading_time,

    a.scraped_at

FROM articles a

JOIN sources s
ON a.source_id = s.source_id

JOIN categories c
ON a.category_id = c.category_id;

-- 2. The Article -- Authors relationship

CREATE OR REPLACE VIEW vw_article_authors AS
SELECT

    a.article_id,
    a.title,

    s.source_name,

    au.author_id,
    au.display_name

FROM articles a

JOIN sources s
ON a.source_id = s.source_id

JOIN article_authors aa
ON a.article_id = aa.article_id

JOIN authors au
ON aa.author_id = au.author_id;

-- 3. The Article - Companies relationship

CREATE OR REPLACE VIEW vw_article_companies AS
SELECT

    a.article_id,
    a.title,

    s.source_name,

    comp.company_name,

    a.published_at

FROM articles a

JOIN sources s
ON a.source_id = s.source_id

JOIN article_companies ac
ON a.article_id = ac.article_id

JOIN companies comp
ON ac.company_id = comp.company_id;

-- 4. The Article Technology view

CREATE OR REPLACE VIEW vw_article_technologies AS
SELECT

    a.article_id,
    a.title,

    s.source_name,

    tech.technology_name,

    a.published_at

FROM articles a

JOIN sources s
ON a.source_id = s.source_id

JOIN article_technologies at
ON a.article_id = at.article_id

JOIN technologies tech
ON at.technology_id = tech.technology_id;

-- 5. The article tags view

CREATE OR REPLACE VIEW vw_article_tags AS
SELECT

    a.article_id,
    a.title,

    s.source_name,

    t.tag_name,

    a.published_at

FROM articles a

JOIN sources s
ON a.source_id = s.source_id

JOIN article_tags atg
ON a.article_id = atg.article_id

JOIN tags t
ON atg.tag_id = t.tag_id;


-- Checking and validation

SELECT * FROM vw_article_master LIMIT 10;

SELECT * FROM vw_article_authors LIMIT 10;

SELECT * FROM vw_article_companies LIMIT 10;

SELECT * FROM vw_article_technologies LIMIT 10;

SELECT * FROM vw_article_tags LIMIT 10;