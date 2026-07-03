

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


