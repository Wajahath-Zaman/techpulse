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

Currently in progress.

---

## Upcoming Phases

- Database Implementation
- Web Scraper Development
- ETL Pipeline
- SQL Analytics
- Python Analysis & NLP
- Tableau Dashboard
- Automation
- Deployment

---

## Documentation

- Business Requirements Document
- System Architecture Document
- Database Design Specification
- Entity Relationship Diagram (ERD)

---

## Project Status

🚧 **Currently Under Development**

The project is currently transitioning from the design phase to implementation. Database development will begin next, followed by web scraping, ETL development, analytical processing, and interactive dashboard creation.

---

## Author

**Mohammad Wajahath Uz Zaman**

M.Tech – Robotics & Artificial Intelligence

Aspiring Data Analyst | Data Engineer | Business Intelligence Developer