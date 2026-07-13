/*
==========================================================
TECHPULSE SQL ANALYTICS
==========================================================
*/

-- Q1. How many articles has techpulse collected ? 

SELECT 
	count(*) as Total_number_of_articles
FROM 
	articles;
    
-- Q2. Which publishers contribute the most articles ?

SELECT 
	s.source_name,
	count(a.article_id) as No_of_articles
FROM 
	articles AS a
JOIN sources AS s
ON a.source_id = s.source_id
GROUP BY source_name;    


-- Q3. Which Technology Categories dominate the news ?

SELECT 
	c.category_name,
    count(a.article_id) AS no_of_articles
FROM 
	articles AS a
JOIN categories AS c
ON a.category_id = c.category_id
WHERE category_name <> ""
GROUP BY category_name
ORDER BY no_of_articles DESC;

-- Q4. How many unique authors have contributed articles ?

SELECT 
	COUNT(DISTINCT author_id) AS Total_Unique_Authors
FROM 
	authors;

-- 05. What is the data range of the collected articles ?

SELECT 
	min(created_at) as Start_date,
    max(created_at) as Recent_date,
    DateDiff(max(created_at), min(created_at)) AS Range_in_days
FROM articles;

-- 06. What percentage of total articles does each publisher contribute ?

SELECT 
    s.source_name,
    COUNT(a.article_id) AS No_of_articles,
    ROUND(
        COUNT(a.article_id) * 100.0 / SUM(COUNT(a.article_id)) OVER (), 
        2
    ) AS Percentage_of_total
FROM 
    articles AS a
JOIN sources AS s
    ON a.source_id = s.source_id
GROUP BY s.source_name
ORDER BY No_of_articles DESC;

-- Q7. Which Publisher has the highest average reading time ?

SELECT * FROM articles;

SELECT
	s.source_name,
    ROUND(AVG(a.reading_time)) AS average_reading_time_in_minutes
FROM articles AS a
JOIN sources AS s
ON a.source_id = s.source_id
GROUP BY source_name
ORDER BY sum(a.reading_time) DESC;

-- Q8. How many categories does each publisher cover ?

SELECT 
	s.source_name,
    count(DISTINCT category_id) AS Total_Unique_Categories
FROM
	articles AS a
JOIN sources AS s
ON a.source_id = s.source_id
GROUP BY source_name
ORDER BY count(DISTINCT category_id) DESC;


-- Q9. What Categories Contain the Highest Number of articles ?

SELECT 
	c.category_name,
    COUNT(a.article_id) as Total_no_of_articles
FROM 
	articles AS a
JOIN categories AS c
ON a.category_id = c.category_id
GROUP BY category_name
ORDER BY COUNT(a.article_id) DESC;

-- 10Q. Which Categories have the longest average articles ?

SELECT 
	c.category_name,
    FLOOR(AVG(a.word_count)) AS Average_Length
FROM 
	articles AS a
JOIN categories AS c
ON a.category_id = c.category_id
GROUP BY category_name
ORDER BY AVG(a.word_count) DESC;

-- 11Q. Which Categories require the highest Average Reading Time ?

SELECT 
	c.category_name,
    ROUND(AVG(a.reading_time)) as Average_reading_timne
FROM 
	articles AS a
JOIN categories AS c
ON a.category_id = c.category_id
GROUP BY category_name
ORDER BY AVG(a.reading_time) DESC;

-- 12Q. Which Publishers Dominate Each Category ?

# We need to present Each Category in the first column
# Then we need to present the dominating publisher in the second column
# We can use ranking here

SELECT 
	category_name,
    source_name
FROM
( SELECT
	c.category_name,
    s.source_name,
    DENSE_RANK() OVER (PARTITION BY c.category_name ORDER BY COUNT(a.article_id) DESC) AS Dominance_Ranking
FROM 
	articles AS a
JOIN sources AS s
ON a.source_id = s.source_id
JOIN categories AS c
ON a.category_id = c.category_id
WHERE c.category_name <> ""
GROUP BY c.category_name, s.source_name) AS X
WHERE Dominance_Ranking = 1;


-- Q13. Who are the most active authors ?

SELECT 
	au.display_name AS Author_name,
    COUNT(a.article_id) AS no_of_articles
FROM 
	articles AS a
JOIN article_authors as a_au 
ON a.article_id = a_au.article_id
JOIN authors AS au
ON a_au.author_id = au.author_id
GROUP BY au.display_name
ORDER BY COUNT(a.article_id) DESC;

-- Q14. Which Authors Publish across multiple Categories ?

SELECT 
	au.display_name AS Author_name,
    COUNT(DISTINCT c.category_id) AS Total_Unique_Categories
FROM 
	articles AS a
JOIN article_authors AS a_au
ON a.article_id = a_au.article_id
JOIN authors AS au
ON a_au.author_id = au.author_id
JOIN categories AS c
ON a.category_id = c.category_id
GROUP BY au.display_name
ORDER BY COUNT(DISTINCT c.category_id) DESC;

-- Q15. Which publishers have the largest number of unique authors ?

# We need to get the list of publishers as well as the authors associated with them

SELECT
	s.source_name,
    COUNT(DISTINCT au.display_name) AS no_of_unique_authors
FROM 
	articles AS a
JOIN sources AS s
ON a.source_id = s.source_id
JOIN article_authors AS a_au
ON a.article_id = a_au.article_id
JOIN authors AS au
ON a_au.author_id = au.author_id
GROUP BY s.source_name
ORDER BY COUNT(DISTINCT au.display_name) DESC;


-- Q16. Which publisher is growing the fastest over time ?

# First get the total number of articles for each publisher for each day
# Then Calculate the growth percentage for each day
# Then take the median of growth percentage

WITH CTE1 AS (
SELECT 
	s.source_name,
    DATE(a.created_at) AS publish_date,
    COUNT(a.article_id) AS article_count
FROM 
	articles AS a
JOIN sources AS s
ON a.source_id = s.source_id
GROUP BY source_name, publish_date
),

CTE2 AS (
SELECT 
	*,
    ROUND((article_count - LAG(article_count,1) OVER (PARTITION BY source_name ORDER BY publish_date)) * 100 / 
    LAG(article_count,1) OVER (PARTITION BY source_name ORDER BY publish_date),2) AS growth_percentage
FROM 
	CTE1
ORDER BY source_name, publish_date
),

CTE3 AS 
(SELECT 
	*,
    LEAST(growth_percentage,100) AS capped_growth_percentage
FROM 
	CTE2)
    
SELECT 
	source_name,
    ROUND(AVG(capped_growth_percentage),2) as Average_capped_growth_percentage
FROM 
	CTE3
GROUP BY source_name;
    

-- Q17. Calculate the running total of articles over time ?

# First we need to get the total articles published in each day.
# Then we will get the running sum of the no of articles

WITH cte1 AS (
SELECT 
	DATE(created_at) AS publish_date,
    COUNT(article_id) AS No_of_articles
FROM articles
GROUP BY publish_date)

SELECT 
	*,
    SUM(No_of_articles) OVER (ORDER BY publish_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM
	cte1;
    
	
-- Q18. Compare daily article Count With the previous day ?

# First Get the total number of published articles for each day. 
# Then compare it with previous day after ordering the data

WITH CTE1 AS (
SELECT 
	DATE(created_at) AS publish_date,
    COUNT(article_id) AS No_of_articles
FROM
	articles
GROUP BY publish_date
)

SELECT
	*,
    LAG(No_of_articles,1) OVER (ORDER BY publish_date) AS previous_day_article_count
FROM 
	CTE1
ORDER BY publish_date;

