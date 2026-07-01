# Data Dictionary

## Project Information

| Field | Value |
|--------|-------|
| Project | TechPulse – Tech News Analytics Platform |
| Document | Data Dictionary |
| Version | 1.0 |
| Status | Complete |

---

# Purpose

This document provides a detailed description of every table and column within the TechPulse database. It serves as a reference for developers, data analysts, and data engineers by documenting the database schema, constraints, relationships, and intended use of each attribute.

---

# Database Overview

The TechPulse database is designed using normalization principles to minimize redundancy and maintain data integrity. The schema consists of lookup tables, a central fact table, bridge tables to resolve many-to-many relationships, and an operational logging table.

---

# Table: sources

## Purpose

Stores information about the technology news publishers from which articles are collected.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| source_id | INT | PK, AUTO_INCREMENT | Unique source identifier |
| source_name | VARCHAR(100) | NOT NULL, UNIQUE | Publisher name |
| website_url | VARCHAR(255) | NOT NULL, UNIQUE | Official website |
| rss_feed_url | VARCHAR(255) | UNIQUE | RSS feed URL |
| country | VARCHAR(100) | NULL | Publisher country |
| language | CHAR(2) | NOT NULL | ISO language code |
| is_active | BOOLEAN | DEFAULT TRUE | Enables or disables scraping |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | AUTO UPDATE | Last update timestamp |

---

# Table: categories

## Purpose

Stores standardized article categories.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| category_id | INT | PK | Unique category identifier |
| category_name | VARCHAR(100) | UNIQUE | Category name |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

---

# Table: authors

## Purpose

Stores author information for scraped articles.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| author_id | INT | PK | Unique author identifier |
| source_id | INT | FK | Associated publisher |
| display_name | VARCHAR(150) | NOT NULL | Author name as published |
| profile_url | VARCHAR(255) | NULL | Author profile page |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

---

# Table: companies

## Purpose

Stores companies mentioned in articles.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| company_id | INT | PK | Company identifier |
| company_name | VARCHAR(150) | UNIQUE | Company name |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

---

# Table: technologies

## Purpose

Stores technologies mentioned in articles.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| technology_id | INT | PK | Technology identifier |
| technology_name | VARCHAR(150) | UNIQUE | Technology name |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

---

# Table: tags

## Purpose

Stores article tags.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| tag_id | INT | PK | Tag identifier |
| tag_name | VARCHAR(100) | UNIQUE | Tag name |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

---

# Table: articles

## Purpose

Stores all scraped technology news articles.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| article_id | INT | PK | Unique article identifier |
| article_url | VARCHAR(1000) | UNIQUE | Original article URL |
| source_id | INT | FK | Publisher |
| category_id | INT | FK | Article category |
| title | VARCHAR(300) | NOT NULL | Article title |
| summary | TEXT | NULL | Article summary |
| content | LONGTEXT | NULL | Full article content |
| published_at | DATETIME | NULL | Original publication date |
| scraped_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Last scrape timestamp |
| word_count | INT | NULL | Number of words |
| reading_time | SMALLINT | NULL | Estimated reading time (minutes) |
| content_hash | CHAR(64) | NOT NULL | SHA-256 hash of article content |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | AUTO UPDATE | Last update time |

---

# Table: article_authors

## Purpose

Maps articles to their authors.

| Column | Data Type | Constraints |
|----------|-----------|-------------|
| article_id | INT | PK, FK |
| author_id | INT | PK, FK |

---

# Table: article_companies

## Purpose

Maps articles to companies mentioned.

| Column | Data Type | Constraints |
|----------|-----------|-------------|
| article_id | INT | PK, FK |
| company_id | INT | PK, FK |

---

# Table: article_technologies

## Purpose

Maps articles to technologies mentioned.

| Column | Data Type | Constraints |
|----------|-----------|-------------|
| article_id | INT | PK, FK |
| technology_id | INT | PK, FK |

---

# Table: article_tags

## Purpose

Maps articles to associated tags.

| Column | Data Type | Constraints |
|----------|-----------|-------------|
| article_id | INT | PK, FK |
| tag_id | INT | PK, FK |

---

# Table: scrape_logs

## Purpose

Stores execution details for every scraping run.

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| log_id | INT | PK | Log identifier |
| source_id | INT | FK | Scraped source |
| scrape_started_at | TIMESTAMP | NOT NULL | Start time |
| scrape_completed_at | TIMESTAMP | NULL | Completion time |
| articles_found | INT | DEFAULT 0 | Total articles discovered |
| articles_inserted | INT | DEFAULT 0 | Successfully inserted articles |
| status | ENUM | NOT NULL | SUCCESS, FAILED, PARTIAL |
| error_message | TEXT | NULL | Error details |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Log creation time |