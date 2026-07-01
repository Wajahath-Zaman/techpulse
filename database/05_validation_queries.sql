

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

