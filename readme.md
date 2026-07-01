# TechPulse

> **An End-to-End Tech News Analytics Platform**

TechPulse is a production-style data analytics platform that automatically collects technology news from multiple online publishers, processes the data through a modern Medallion Architecture, stores it in a relational database, performs analytical transformations, and visualizes business insights through interactive Tableau dashboards.

The project demonstrates the complete data analytics lifecycle, from data acquisition to business intelligence, using real-world continuously updating data.

---

## Project Objectives

- Collect technology news from multiple online sources.
- Build an automated data ingestion pipeline.
- Preserve historical versions of news articles.
- Design a scalable relational database.
- Perform SQL and Python-based analysis.
- Visualize trends using Tableau.
- Demonstrate real-world Data Analytics and Data Engineering practices.

---

## System Architecture

```
Technology News Websites
           │
           ▼
     Python Web Scrapers
           │
           ▼
   Bronze Layer (Raw Data)
           │
           ▼
       ETL Pipeline
           │
           ▼
Silver Layer (Clean & Normalized)
           │
           ▼
 Gold Layer (Analytics Ready)
           │
      ┌────┴────┐
      ▼         ▼
 SQL Analytics  Python Analytics
      │         │
      └────┬────┘
           ▼
    Tableau Dashboard
```

---

## Medallion Architecture

### Bronze Layer

- Stores raw scraped data.
- Preserves original articles.
- Acts as the source of truth.
- Supports data recovery and reprocessing.

### Silver Layer

- Cleans and standardizes data.
- Removes duplicates.
- Maintains normalized relational tables.
- Preserves article version history.

### Gold Layer

- Generates analytical datasets.
- Produces KPIs and business metrics.
- Optimized for SQL analysis and Tableau dashboards.

---

## Planned Database Design

The relational database follows normalization principles and consists of:

### Core Tables

- Sources
- Articles
- Article Versions
- Categories
- Authors
- Companies
- Technologies
- Tags

### Bridge Tables

- Article Authors
- Article Companies
- Article Technologies
- Article Tags

### Operational Tables

- Scrape Logs

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Web Scraping | Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy |
| Database | MySQL |
| ORM | SQLAlchemy |
| Analytics | SQL, Python |
| NLP | spaCy, NLTK |
| Visualization | Tableau Public |
| Version Control | Git, GitHub |

---

## Project Structure

```
TechPulse/
│
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── archive/
│
├── database/
│   ├── 01_create_database.sql
│   └── 02_create_tables.sql
│
├── docs/
│   ├── 01_business_requirements.md
│   ├── 02_system_architecture.md
│   ├── 03_database_design_specification.md
│   └── images/
│
├── scrapers/
├── etl/
├── analysis/
├── dashboard/
├── notebooks/
├── reports/
├── tests/
└── README.md
```

---

## Current Progress

### ✅ Phase I – Project Setup

- Project structure created
- Git repository initialized
- Virtual environment configured
- Dependencies installed
- Initial documentation prepared

### ✅ Phase II – Business Understanding

- Business problem defined
- Project objectives identified
- Data sources selected
- High-level data pipeline designed

### ✅ Phase III – System & Database Design

- Medallion Architecture designed
- End-to-end system architecture documented
- Database architecture finalized
- Entity Relationship Diagram (ERD) created
- Database Design Specification completed

### 🔄 Phase IV – Database Implementation


The database layer has been fully designed and implemented using MySQL. The schema follows normalization principles and serves as the foundation for the entire analytics pipeline.

#### Completed Tasks

- Designed and implemented a normalized relational database.
- Created all core entity tables.
- Implemented bridge tables to resolve many-to-many relationships.
- Added primary keys, foreign keys, and integrity constraints.
- Created indexes to improve query performance.
- Developed reusable SQL views for analytical queries.
- Prepared seed data for testing and development.
- Validated database relationships and schema integrity.

#### Database Schema

The database currently contains the following tables:

##### Core Tables

- Sources
- Categories
- Authors
- Companies
- Technologies
- Tags
- Articles
- Scrape Logs

##### Bridge Tables

- Article Authors
- Article Companies
- Article Technologies
- Article Tags

#### Key Features

- Fully normalized relational database (3NF)
- Referential integrity using foreign keys
- Optimized indexing strategy
- Reusable SQL views
- Many-to-many relationship modeling
- Designed for scalable web scraping and analytics

#### Current Project Status

- ✅ Project Setup
- ✅ Business Requirements
- ✅ System Architecture
- ✅ Database Design
- ✅ Database Implementation
- ⏳ Web Scraper Development (Next Phase)
---


## Project Status

🚧 **Currently Under Development**

The project is currently transitioning from the design phase to implementation. Database development will begin next, followed by web scraping, ETL development, analytical processing, and interactive dashboard creation.

---

## Author

**Mohammad Wajahath Uz Zaman**

M.Tech – Robotics & Artificial Intelligence

Aspiring Data Analyst | Data Engineer | Business Intelligence Developer