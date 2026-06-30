I think this is the right place to **slow down and do it properly**. This document will become the blueprint for the entire project. Every future decision (SQL, ETL, scraping, analytics) should align with it.

I also suggest a slight rename:

```
docs/
    database_design_specification.md
```

rather than keeping it under `database/`. This is a design document, not an implementation artifact. Later, your `database/` folder can contain only SQL scripts.

---

# Database Design Specification

## 1. Document Information

| Field    | Value                                                                                                                |
| -------- | -------------------------------------------------------------------------------------------------------------------- |
| Project  | TechPulse – Tech News Analytics Platform                                                                             |
| Document | Database Design Specification                                                                                        |
| Version  | 1.0                                                                                                                  |
| Status   | Draft                                                                                                                |
| Author   | Mohammad Wajahath Uz Zaman                                                                                           |
| Purpose  | Define the database architecture, data layers, entities, relationships, and design principles before implementation. |

---

# 2. Purpose

The purpose of this document is to define the logical database architecture for the TechPulse platform before implementation. It describes how data will be stored, transformed, and consumed throughout the analytics pipeline.

The document serves as a blueprint for database development and ensures consistency between the scraping pipeline, ETL process, SQL analysis, and visualization layer.

---

# 3. Database Objectives

The database has been designed to:

* Store technology news from multiple publishers.
* Preserve historical versions of articles.
* Support large-scale analytical queries.
* Eliminate data redundancy through normalization.
* Maintain referential integrity.
* Support incremental data ingestion.
* Enable future expansion with additional publishers.
* Provide analytics-ready datasets for reporting.

---

# 4. Database Architecture

The TechPulse platform follows the **Medallion Architecture**, consisting of three logical layers.

```text
                News Websites
                      │
                      ▼
            Bronze Layer (Raw Data)
                      │
                      ▼
      Silver Layer (Clean & Normalized)
                      │
                      ▼
     Gold Layer (Business Analytics)
                      │
                      ▼
              Tableau Dashboard
```

Each layer has a distinct responsibility within the data pipeline.

---

# 5. Layer Descriptions

## 5.1 Bronze Layer

### Purpose

The Bronze layer stores raw data exactly as it is collected from external news websites. No business rules or transformations are applied at this stage.

### Characteristics

* Raw scraped data
* Immutable records
* Original article content
* Original metadata
* Source of truth
* Used for recovery and reprocessing

### Expected Tables

| Table              | Purpose                |
| ------------------ | ---------------------- |
| bronze_articles    | Raw article data       |
| bronze_scrape_logs | Scraper execution logs |

---

## 5.2 Silver Layer

### Purpose

The Silver layer contains cleaned, standardized, and normalized data. This layer forms the operational database used by analysts and downstream processes.

### Characteristics

* Cleaned data
* Duplicate removal
* Standardized dates
* Standardized text
* Normalized entities
* Historical article versions

### Expected Tables

| Table                | Purpose                |
| -------------------- | ---------------------- |
| articles             | Master article records |
| article_versions     | Version history        |
| sources              | News publishers        |
| authors              | Authors                |
| article_authors      | Bridge table           |
| categories           | Categories             |
| companies            | Companies              |
| article_companies    | Bridge table           |
| technologies         | Technologies           |
| article_technologies | Bridge table           |
| tags                 | Tags                   |
| article_tags         | Bridge table           |

---

## 5.3 Gold Layer

### Purpose

The Gold layer stores business-ready datasets generated from the Silver layer. These datasets are optimized for analytical queries and dashboard visualization.

### Characteristics

* Aggregated metrics
* Trend analysis
* KPI calculations
* Reporting tables
* Dashboard optimization

### Expected Tables

| Table                 | Purpose                   |
| --------------------- | ------------------------- |
| daily_article_metrics | Daily KPIs                |
| company_trends        | Company trend analysis    |
| technology_trends     | Technology trend analysis |
| source_metrics        | Publisher metrics         |
| category_metrics      | Category metrics          |

---

# 6. Database Design Principles

The following principles guide the design of the TechPulse database:

### Normalization

The database follows normalization principles to reduce redundancy and improve consistency.

---

### Surrogate Keys

Every entity uses an auto-increment integer primary key.

Business identifiers such as URLs are stored as unique attributes rather than primary keys.

---

### Referential Integrity

Relationships between entities are enforced using foreign key constraints.

---

### Historical Preservation

Article history is preserved through versioning rather than overwriting existing records.

---

### Scalability

The schema is designed to support additional publishers, categories, and entities without structural changes.

---

### Data Quality

Uniqueness constraints and validation rules are applied wherever appropriate to maintain data integrity.

---

# 7. Entity Relationships

The Silver layer represents the core relational model.

The following relationships exist:

| Parent   | Relationship | Child            |
| -------- | ------------ | ---------------- |
| Source   | One-to-Many  | Articles         |
| Category | One-to-Many  | Articles         |
| Article  | One-to-Many  | Article Versions |
| Article  | Many-to-Many | Authors          |
| Article  | Many-to-Many | Companies        |
| Article  | Many-to-Many | Technologies     |
| Article  | Many-to-Many | Tags             |

Many-to-many relationships are resolved using bridge tables.

---

# 8. Naming Conventions

The following naming standards are adopted:

* Table names use `snake_case`.
* Primary keys follow the pattern `<table>_id`.
* Foreign keys reference the parent table's primary key.
* Bridge tables combine entity names (e.g., `article_tags`).
* Boolean columns use prefixes such as `is_` or `has_`.
* Timestamp fields use UTC.
* Singular entity names are used throughout the schema.

---

# 9. Data Flow

```text
News Website
      │
      ▼
Python Scraper
      │
      ▼
Bronze Layer
      │
      ▼
Cleaning & Standardization
      │
      ▼
Silver Layer
      │
      ▼
Aggregation & Business Logic
      │
      ▼
Gold Layer
      │
      ▼
Tableau Dashboard
```

---

# 10. Future Enhancements

The architecture supports future integration of:

* Additional news publishers.
* AI-generated article summaries.
* Named Entity Recognition (NER).
* Sentiment analysis.
* Topic modeling.
* Real-time streaming pipelines.
* Machine learning models for trend prediction.

---

# 11. Conclusion

The TechPulse database has been designed using modern data engineering principles. The Medallion Architecture separates raw, cleaned, and analytical data into independent layers, improving maintainability, scalability, and analytical flexibility. This design provides a strong foundation for implementing the scraping pipeline, ETL processes, SQL analysis, and business intelligence dashboards.

---

## My Recommendation

This is **far stronger** than a typical portfolio project's documentation. After this, our next documents should be:

```
docs/
│
├── business_requirements.md          ✅
├── database_design_specification.md  ✅
├── data_dictionary.md                ⬜
├── architecture.md                   ⬜
├── etl_design.md                     ⬜
└── deployment.md                     ⬜
```

By the time we start writing SQL, you'll have documentation that's very similar to what you'd see in a real analytics or data engineering project, and every implementation decision will be traceable back to a design document.
