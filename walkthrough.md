Excellent. We're going to build this as if you're working as a Data Analyst/Data Engineer in a company. Every step should be production-quality and portfolio-worthy.

---

# Phase 1: Project Setup

## Step 1.1 — Create the Project Folder

Create a new folder named:

```text
TechPulse
```

Open it in **VS Code**.

Your folder should initially look like:

```text
TechPulse/
```

---

# Step 1.2 — Initialize Git

Open the terminal in VS Code.

Run:

```bash
git init
```

You should see something like:

```
Initialized empty Git repository...
```

---

# Step 1.3 — Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

If successful, your terminal will look like:

```text
(.venv) C:\Users\...
```

---

# Step 1.4 — Create the Folder Structure

Inside **TechPulse**, create the following folders.

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

### Why these folders?

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

This structure scales well as the project grows.

---

# Step 1.5 — Create Essential Files

In the project root, create:

```text
README.md

requirements.txt

.gitignore

LICENSE

main.py
```

We'll add more files later as needed.

---

# Step 1.6 — Create the `.gitignore`

Paste the following:

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

Notice that we're **not** committing scraped data by default. The repository will contain the code, not potentially large datasets. We can later include a small sample dataset for demonstration.

---

# Step 1.7 — Add `.gitkeep` Files

Git doesn't track empty folders.

Create empty files named:

```text
data/raw/.gitkeep

data/processed/.gitkeep

data/archive/.gitkeep

logs/.gitkeep

reports/.gitkeep

tests/.gitkeep
```

---

# Step 1.8 — Install Required Libraries

Run:

```bash
pip install requests beautifulsoup4 pandas numpy sqlalchemy pymysql lxml python-dotenv tqdm matplotlib nltk spacy jupyter
```

Then save the installed packages:

```bash
pip freeze > requirements.txt
```

---

# Step 1.9 — Create a Simple `README.md`

Start with:

```markdown
# TechPulse

An end-to-end Tech News Analytics Platform that collects, stores, analyzes, and visualizes technology news from multiple sources.

## Tech Stack

- Python
- BeautifulSoup
- Requests
- MySQL
- SQLAlchemy
- Pandas
- Tableau
- Git

## Project Status

🚧 Under Development
```

We'll expand this into a professional README as the project evolves.

---

# Step 1.10 — First Git Commit

Stage everything:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial project setup"
```

---

# What We'll Build Next

Once this setup is complete, we'll move to **Phase 2: System Design**, where we'll define the database schema, the scraping architecture, and the ETL workflow before writing any scraper.

We'll also decide on the news sources, the update frequency, and how to handle duplicates and incremental updates.

## A Small Improvement

Compared to many tutorial projects, I'd like us to treat this like a real software project from the beginning. One thing I recommend is creating a `src/` directory to hold all Python code instead of placing scripts at the project root. For example:

```text
TechPulse/
│
├── src/
│   ├── scrapers/
│   ├── etl/
│   ├── analysis/
│   └── utils/
```

This is a common industry practice and keeps the repository organized as it grows. It will also make packaging and testing easier later.


Absolutely. I want you to understand **why** we're doing each step, not just follow instructions. That's how you'll be able to explain your project confidently in interviews.

---

# 1. Creating the Project Folder (`TechPulse`)

```
TechPulse/
```

### Why?

This is the root of your project. Everything related to TechPulse lives here.

Think of it like building a house. Before constructing rooms, you first buy the land.

This folder will eventually contain:

* Code
* Database scripts
* Data
* Documentation
* Dashboard
* Reports

Recruiters should be able to clone one repository and find everything.

---

# 2. Initializing Git

```bash
git init
```

### Why?

Git is a version control system.

Imagine this scenario:

You spend 3 weeks building the scraper.

Then one day you make a mistake.

Everything breaks.

Without Git:

❌ You lose your previous working code.

With Git:

✅ You simply go back to yesterday's version.

---

### It also shows recruiters

This is important.

Companies don't just look at the final code.

They like seeing the development history.

Example:

```
Initial project setup

Added TechCrunch scraper

Added MySQL integration

Implemented ETL pipeline

Added NLP sentiment analysis

Created Tableau dashboard
```

This tells recruiters:

> "This person knows professional software development."

---

# 3. Creating a Virtual Environment

```
python -m venv .venv
```

### Why?

Every Python project needs libraries.

Example:

Project A

```
Pandas 2.0
```

Project B

```
Pandas 1.4
```

Without a virtual environment,

both projects would use the same installation.

That creates dependency conflicts.

---

A virtual environment isolates your project.

Think of it like giving each project its own mini Python installation.

```
Windows

Python
    │
    ├── Project A
    │      pandas 2.0
    │
    └── Project B
           pandas 1.4
```

No conflicts.

---

# 4. Folder Structure

This is probably the most important step.

Instead of dumping everything here:

```
scraper.py

analysis.py

dashboard.py

mysql.py

test.py

script2.py

new.py

temp.py
```

(which becomes chaos after a month)

We organize by responsibility.

---

## data/

```
data/
```

Stores all datasets.

---

### raw/

```
data/raw/
```

Original scraped articles.

Never modify these.

Example:

```
{
"title":"OpenAI launches...",
"content":"..."
}
```

These are your "source of truth."

---

### processed/

Contains cleaned data.

Example:

Original

```
Title:
" OPENAI launches GPT "

Date:
"June 25th, 2026"

```

After cleaning

```
title

date

source
```

Standardized.

---

### archive/

Suppose tomorrow

TechCrunch deletes an article.

You still have yesterday's copy.

This folder stores historical snapshots.

---

# scrapers/

Contains scraping code.

Later it may look like:

```
scrapers/

techcrunch.py

theverge.py

arstechnica.py

wired.py

common.py
```

Each website has different HTML.

Keeping them separate makes maintenance much easier.

---

# database/

Everything related to SQL.

Example:

```
schema.sql

views.sql

indexes.sql

stored_procedures.sql
```

Instead of hiding SQL inside Python.

---

# etl/

ETL stands for

Extract

↓

Transform

↓

Load

Example:

Extract

↓

Scrape article

↓

Transform

↓

Clean text

↓

Convert dates

↓

Remove duplicates

↓

Load

↓

Insert into MySQL

---

Keeping ETL separate is exactly how many companies organize their data pipelines.

---

# analysis/

After data is in MySQL,

this folder answers business questions.

Examples:

```
trend_analysis.py

company_analysis.py

technology_analysis.py

sentiment_analysis.py
```

Notice:

Analysis

≠

Scraping

Different responsibilities.

---

# dashboard/

Stores Tableau workbooks.

```
dashboard/

TechPulse.twb

Screenshots/

Exports/
```

---

# notebooks/

Jupyter notebooks.

Good for exploration.

Later,

once code becomes stable,

move it into Python scripts.

This is common in data teams:

* Notebook for exploration
* Python scripts for production

---

# reports/

Suppose every Monday

you generate

```
Weekly AI Report.pdf
```

Store it here.

---

# logs/

Every professional application has logs.

Instead of seeing

```
Something went wrong
```

You see:

```
2026-06-28 08:10

Connected

Downloaded page

Parsed article

Inserted into database

Success
```

If scraping fails,

you know exactly where.

---

# config/

Never hardcode things like:

```
Database password

API key

Website URLs

Scrape interval
```

Instead,

keep configuration separate.

Makes updating easier.

---

# tests/

Professional software is tested.

Later we'll write tests like:

```
Does the parser correctly extract the title?

Yes

Pass
```

---

# docs/

Documentation.

Contains

Architecture

ER Diagram

Flowcharts

Screenshots

Business requirements

Interviewers appreciate good documentation because it shows you can communicate technical work clearly.

---

# 5. README.md

This is the homepage of your GitHub repository.

When someone opens your repository,

this is the first thing they see.

A good README answers:

* What is this project?
* Why did you build it?
* What technologies are used?
* How do I run it?
* What insights does it provide?

Many recruiters decide whether to explore a repository further based on the README.

---

# 6. requirements.txt

Suppose I clone your project.

How do I know which libraries you used?

I don't.

But with

```
requirements.txt
```

I simply run

```bash
pip install -r requirements.txt
```

and my environment matches yours.

---

# 7. .gitignore

Some files should **not** be pushed to GitHub.

Examples:

```
Passwords

Virtual environment

Python cache

Logs

Temporary files
```

`.gitignore` tells Git:

> "Ignore these files."

Without it,

people accidentally upload thousands of unnecessary files—or even secrets.

---

# 8. .gitkeep

Git doesn't track empty folders.

Suppose

```
logs/
```

is empty.

Git ignores it.

Adding an empty

```
.gitkeep
```

file forces Git to preserve the folder structure.

---

# 9. Installing Packages

```
requests

beautifulsoup4

pandas

sqlalchemy

...
```

We're building the project's toolbox.

Each package has a specific job:

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
| `jupyter`        | Interactive notebooks for exploration                    |

---

# 10. First Commit

```
git commit
```

This is your **first checkpoint**.

If tomorrow something breaks,

you can always return to this clean starting point.

---

## Why I Suggested `src/`

At the end, I suggested adding a `src/` directory. This is a common practice in larger Python projects because it clearly separates your application code from everything else.

Instead of:

```text
TechPulse/
├── scrapers/
├── analysis/
├── etl/
```

you might have:

```text
TechPulse/
├── src/
│   ├── scrapers/
│   ├── etl/
│   ├── analysis/
│   └── utils/
├── data/
├── docs/
├── tests/
```

This keeps all Python modules in one place and makes imports, testing, and packaging cleaner as the project grows.

---

## One More Thing

As we build this project, I won't just tell you **what** to do. I'll explain the reasoning behind each design decision, point out common alternatives, and discuss why we're choosing one approach over another. That way, when an interviewer asks, *"Why did you normalize your database?"* or *"Why did you separate ETL from scraping?"*, you'll be able to answer with confidence rather than saying, *"I followed a tutorial."*


## Day - 2

Excellent! 🎉

You've just completed something many beginners skip: you've created a **clean baseline** for the project. From this point onward, every meaningful feature will have its own commit, giving you a professional development history.

---

# Phase 2: System Design

Before writing a single scraper, we're going to answer an important question:

> **How will data flow through our system?**

Many people start coding immediately. Six weeks later, they have:

* Duplicate data
* Poor database design
* Scrapers that don't scale
* Difficult-to-maintain code

We're going to avoid all of that.

---

# Step 2.1 – Define the Data Pipeline

Our pipeline will look like this:

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

Let's understand each stage.

### 1. News Websites

These are our data sources.

Examples:

* TechCrunch
* The Verge
* Ars Technica
* Hacker News (different structure)
* Company engineering blogs

Each source has a different HTML structure, so we'll build a scraper for each one.

---

### 2. Web Scraper

The scraper's only responsibility is to collect data.

It should **not**:

* Calculate statistics
* Perform sentiment analysis
* Generate dashboards

Its job is simply:

```text
Visit page
    ↓
Extract information
    ↓
Return structured data
```

This separation makes the code easier to test and maintain.

---

### 3. Raw Data (JSON)

Why save raw data before inserting it into the database?

Imagine this scenario:

You scrape **10,000 articles**.

Later you discover your ETL code has a bug.

If you only stored data in MySQL, you might have to scrape all 10,000 articles again.

If you also saved the raw JSON, you can simply rerun the ETL process without hitting the websites again.

---

### 4. ETL Pipeline

The ETL stage transforms raw data into clean, consistent data.

For example:

Raw:

```text
Title: "  OpenAI Launches GPT-6  "
Date: "June 28, 2026"
```

Processed:

```text
title: "OpenAI Launches GPT-6"
publish_date: 2026-06-28
```

This stage also:

* Removes duplicates
* Handles missing values
* Standardizes categories
* Calculates derived fields (word count, reading time, etc.)

---

### 5. MySQL Database

The database becomes the **single source of truth** for analysis.

Instead of repeatedly parsing JSON files, every analysis script queries the database.

Benefits:

* Faster querying
* Easier filtering
* Better data integrity
* Scales to much larger datasets

---

### 6. SQL Analysis

Here we'll answer business questions using SQL.

Examples:

* Which companies are mentioned most?
* Which topics are trending?
* Which source publishes the most AI articles?
* How has AI coverage changed over time?

This is where you'll showcase advanced SQL skills.

---

### 7. Python Analysis & NLP

SQL is excellent for aggregation and filtering.

Python is better for:

* Sentiment analysis
* Keyword extraction
* Named entity recognition
* Topic modeling
* Time-series visualization

The two complement each other.

---

### 8. Tableau Dashboard

Finally, we'll present the insights.

Think of Tableau as the presentation layer.

We'll create dashboards for:

* Executive summary
* Technology trends
* Company mentions
* Publishing activity
* Sentiment trends

---

# Why This Architecture?

Each component has **one responsibility**:

| Component | Responsibility      |
| --------- | ------------------- |
| Scraper   | Collect data        |
| ETL       | Clean and transform |
| Database  | Store data          |
| SQL       | Query and aggregate |
| Python    | Advanced analysis   |
| Tableau   | Visualize           |

This follows the **Single Responsibility Principle**, making the project easier to maintain and extend.

---

# Next Step: Choosing the Sources

Before designing the database, we need to know **what kind of data** we'll be collecting.

We'll decide:

* Which news sources to use
* Whether to scrape HTML or use RSS feeds
* What fields each source provides
* A common schema that works across all sources

This decision will directly influence our database design.

We'll choose sources that are reliable, regularly updated, and provide rich metadata for analysis.


Great! This is one of the most important design decisions in the project.

## Step 2.2 – Choosing Our Data Sources

We have three options.

### Option 1: Scrape HTML pages

* ✅ Full article content
* ✅ More data available
* ❌ More difficult to maintain because websites change their HTML

### Option 2: RSS feeds

* ✅ Easy to parse
* ✅ Very stable
* ✅ Fast
* ❌ Usually contains only summaries, not the full article

### Option 3: Official APIs

* ✅ Clean, structured data
* ✅ Reliable
* ❌ Many APIs have rate limits or paid tiers

---

## Our Approach

We'll use a **hybrid approach**.

**Step 1:** Collect the latest article links from RSS feeds (where available).

**Step 2:** Visit each article page and scrape the detailed information.

This gives us the best of both worlds:

* Reliable discovery of new articles
* Rich article-level data for analysis

---

## Initial Sources

I recommend starting with **four sources**. That's enough to build a substantial dataset without making the project overwhelming.

| Source       | Why we chose it                 |
| ------------ | ------------------------------- |
| TechCrunch   | Startups, AI, funding, big tech |
| The Verge    | Consumer technology and gadgets |
| Ars Technica | Deep technical articles         |
| VentureBeat  | AI, enterprise tech, startups   |

These sources cover different areas of technology, which will make your analyses more interesting.

---

## Common Data Model

Regardless of the source, every article should be converted into the same format before entering the database.

```text
Article
│
├── title
├── url
├── source
├── author
├── publish_date
├── category
├── summary
├── content
├── tags
├── word_count
├── reading_time
├── scraped_at
```

This is called a **common schema**.

Even though every website has a different layout, your downstream code (ETL, SQL, Tableau) only needs to understand one consistent structure.

---

## Project Workflow

For every source, the pipeline will be:

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

Notice that after the "Convert to common schema" step, every source looks identical to the rest of the system.

---

## Why Start with Four Sources?

Imagine beginning with ten websites.

If one changes its HTML, you'll have to debug one scraper while still building nine others. That's a lot of complexity early on.

Starting with four lets you:

* Build a robust architecture.
* Prove the concept.
* Add more sources later with minimal changes.

Because our code will be modular, adding a fifth source later should mostly involve writing one new scraper rather than changing the whole project.

---

## Your First Real Software Engineering Lesson

A beginner often thinks:

> "I'm building a scraper."

An experienced developer thinks:

> "I'm building a **framework** that can support many scrapers."

That's what we're doing. The individual scrapers are just plugins that feed data into the same pipeline.

---

## Next Session

We'll design the **MySQL database from scratch**. We'll identify all the entities (articles, authors, sources, tags, technologies, companies, etc.), normalize the schema, and create an Entity Relationship Diagram (ERD). By the end, you'll understand not just *what* tables we're creating, but *why* they're designed that way. This is one of the strongest skills you can demonstrate in a data analytics portfolio.


Awesome! This is my favorite part because this is where we stop thinking like someone writing SQL queries and start thinking like a **Database Designer**.

A lot of people can write SQL. Far fewer can **design a database**.

---

# Phase 2.1 - Requirements Analysis

Before creating a database, professionals ask one question:

> **"What information does the business need to store?"**

Not,

> "What tables should I create?"

This is a huge difference.

---

## Step 1: Understand the Business

Imagine a company hires us and says:

> "We want a platform that collects technology news from multiple sources and allows analysts to identify trends."

Before touching MySQL, we'd ask:

### What information do we need?

Every article has

* Title
* URL
* Publish Date
* Author
* Source
* Category
* Content
* Summary

Already we have several different types of information.

---

Now let's think deeper.

Suppose we scrape this article:

```
Title:
OpenAI launches GPT-6

Author:
John Smith

Source:
TechCrunch

Category:
Artificial Intelligence

Tags:
OpenAI
GPT
LLM
AI

Published:
2026-06-29
```

Now ask yourself...

### What are the "things" in this system?

Database designers call these **Entities**.

---

# Step 2: Identify Entities

An entity is simply something about which we want to store information.

Looking at the article, we immediately find:

```
Article

Author

Source

Category

Tag
```

Already we have five entities.

---

But let's continue.

Inside the article, it says

```
OpenAI announced GPT-6.

Microsoft invested...

Google responded...
```

Now we discover another entity:

```
Company
```

---

The article also mentions

```
Python

TensorFlow

PyTorch

CUDA
```

Another entity:

```
Technology
```

---

Now our list becomes

```
Article

Author

Source

Category

Tag

Company

Technology
```

Notice something interesting.

**We haven't written a single SQL statement yet.**

Because database design starts with understanding the business.

---

# Step 3: Determine Relationships

Now we ask:

How are these entities connected?

Let's begin.

---

## Relationship 1

One source publishes many articles.

```
TechCrunch

    │

    ├── Article A

    ├── Article B

    └── Article C
```

This means

```
Source

1 ---------∞ Article
```

One-to-many.

---

## Relationship 2

One author writes many articles.

```
John

 │

 ├── AI News

 ├── Startup News

 └── Cloud News
```

Again

```
Author

1 --------∞ Article
```

---

## Relationship 3

One category contains many articles.

```
Artificial Intelligence

      │

      ├── Article

      ├── Article

      └── Article
```

Again

```
Category

1 --------∞ Article
```

---

## Relationship 4

Now it gets interesting.

Suppose

Article A has tags

```
AI

Machine Learning

OpenAI
```

Article B has

```
AI

Cloud

Python
```

Notice

The tag

```
AI
```

belongs to

Article A

AND

Article B.

Likewise,

Article A has multiple tags.

So

```
Article

∞ -------- ∞ Tag
```

This is called a **Many-to-Many Relationship**.

Relational databases can't represent many-to-many directly.

We'll solve this later with a bridge table.

---

## Relationship 5

Companies

```
Article A

mentions

OpenAI

Microsoft

NVIDIA
```

Another article mentions

```
OpenAI

Anthropic
```

Again

```
Article

∞ -------- ∞ Company
```

---

## Relationship 6

Technologies

```
Article

mentions

Python

CUDA

PyTorch
```

Again

```
Article

∞ -------- ∞ Technology
```

---

# Step 4: Think About Future Requirements

This is where beginners and experienced designers differ.

A beginner designs for **today**.

An experienced designer designs for **the future**.

For example:

Today we scrape

```
TechCrunch
```

Tomorrow we add

```
Wired
```

Will our database break?

No.

Because we created a separate

```
Source
```

table.

---

Suppose tomorrow

One article has

5 authors.

Will we support it?

If we design carefully, yes.

---

Suppose tomorrow

We scrape

50 websites.

Still works.

---

Suppose tomorrow

We scrape

100,000 articles/day.

Still works.

---

# Step 5: What Tables Do We Need?

Based on our analysis, I propose the following tables:

### Core Tables

```
sources

authors

categories

articles
```

---

### Lookup Tables

```
tags

companies

technologies
```

---

### Bridge Tables

```
article_tags

article_companies

article_technologies
```

---

### Operational Tables

```
scrape_logs
```

---

Eventually our database will look like

```
techpulse

│

├── articles

├── authors

├── sources

├── categories

├── companies

├── technologies

├── tags

├── article_tags

├── article_companies

├── article_technologies

└── scrape_logs
```

---

# Why Not Put Everything in One Table?

Many beginners do this.

```
articles

id

title

author

source

category

tag1

tag2

tag3

company1

company2

technology1

technology2
```

Looks simple.

It's actually terrible.

Why?

Imagine

OpenAI changes its name (hypothetically).

You now have to update **every article** where "OpenAI" appears.

With a normalized database, you update it in one place.

This reduces:

* Data duplication
* Storage usage
* Update errors
* Maintenance effort

---

# The Most Important Concept Today

We are **not designing tables**.

We are **modeling the real world**.

The database is simply a representation of reality:

* A news source publishes articles.
* Authors write articles.
* Articles belong to categories.
* Articles mention companies.
* Articles discuss technologies.
* Articles have tags.

Once you understand the business, the tables almost design themselves.

---

# 🚀 What We'll Do Next (and This Is the Fun Part)

In the next step, we'll create our **Entity Relationship Diagram (ERD)** before writing any SQL.

We'll literally draw how every table connects to every other table. This is exactly how database architects work in industry. After that, writing the `CREATE TABLE` statements becomes straightforward because the design has already been thought through.

> **Tip:** Don't worry if terms like "bridge table" or "normalization" feel new. We're going to build this schema together, and I'll explain every design decision with practical examples so you'll be able to explain it confidently in an interview.


## Day - 3

Perfect. Since you're already familiar with **normalization, relationships, primary keys, foreign keys, and bridge tables**, we can approach this like professional database designers instead of treating it as a beginner tutorial.

---

# Step 2.2 - Designing the ERD (Entity Relationship Diagram)

Before creating tables, let's identify the **core business entities** and their relationships.

## Our Entities

```text
News Source
Author
Category
Article
Tag
Company
Technology
Scrape Log
```

Now let's connect them.

---

# Entity 1: Source

A source represents where the article came from.

Examples:

* TechCrunch
* Ars Technica
* The Verge
* VentureBeat

Attributes:

```text
Source
------------
source_id (PK)
name
website
rss_url
country
language
is_active
created_at
```

### Relationship

One source publishes many articles.

```text
Source (1)
     |
     |
     |------< Article (∞)
```

---

# Entity 2: Author

Attributes

```text
Author
------------
author_id (PK)
name
profile_url
bio
```

Now here's our **first design decision**.

### Question

Can an article have multiple authors?

The answer is **yes**.

Many tech publications have:

```text
John Doe
&
Jane Smith
```

If we store `author_id` directly in the Articles table, we'll limit ourselves to one author.

Therefore...

Instead of

```text
Articles

author_id
```

we should have

```text
Authors

Article_Authors
```

Relationship

```text
Author
    ∞
     \
      \
       Article_Authors
      /
     /
    ∞
Article
```

This gives us a **many-to-many** relationship and future-proofs the design.

---

# Entity 3: Category

Examples

```text
AI

Cloud

Security

Programming

Startups
```

One category

↓

Many articles

Simple One-to-Many

```text
Category

category_id

name
```

Relationship

```text
Category (1)
      |
      |
      |
      |------< Article (∞)
```

---

# Entity 4: Article

This is our central table.

Attributes

```text
Article
-------------
article_id

title

url

summary

content

published_at

scraped_at

reading_time

word_count

category_id

source_id
```

Notice something.

We **didn't** store:

* author_name
* company_name
* technology_name
* tags

Why?

Because those belong in their own entities.

---

# Entity 5: Tags

Example

```text
AI

OpenAI

Python

LLM

Startup
```

One article

↓

Many tags

One tag

↓

Many articles

Therefore

Many-to-Many

Bridge table

```text
article_tags
```

---

# Entity 6: Companies

Example

```text
OpenAI

Microsoft

NVIDIA

Google

Meta
```

Again

Many-to-Many

Because

One article mentions many companies

One company appears in many articles

Bridge table

```text
article_companies
```

---

# Entity 7: Technologies

Examples

```text
Python

PyTorch

CUDA

TensorFlow

Kubernetes
```

Again

Many-to-Many

Bridge

```text
article_technologies
```

---

# Entity 8: Scrape Logs

This table is often missing in portfolio projects, but it's extremely useful.

Example

```text
scrape_logs

log_id

source_id

started_at

finished_at

articles_found

articles_inserted

status

error_message
```

Why?

Suppose tomorrow

The TechCrunch scraper fails.

Instead of guessing,

you query

```sql
SELECT *
FROM scrape_logs
WHERE status='FAILED';
```

You immediately know:

* Which source failed
* When
* Why
* How many articles were processed before failure

This is a feature you'd expect in production systems.

---

# The Complete ERD

Here's the overall structure:

```text
                         Sources
                            |
                            |
                        (1) |
                            |
                            |
                           (∞)
                         Articles
                     /    |     |     \
                    /     |     |      \
                   /      |     |       \
                  /       |     |        \
          Categories   Article_Authors   Article_Tags
              |              |               |
             (1)            (∞)             (∞)
              |              |               |
             (∞)          Authors           Tags

Articles
    |
    |
Article_Companies
    |
Companies

Articles
    |
    |
Article_Technologies
    |
Technologies

Sources
    |
Scrape_Logs
```

---

# Let's Challenge Our Design

This is something database architects do before writing SQL.

### Scenario 1

Tomorrow an article has **three authors**.

✅ Supported.

---

### Scenario 2

Tomorrow we scrape **100 websites**.

✅ Supported.

---

### Scenario 3

An article mentions **25 companies**.

✅ Supported.

---

### Scenario 4

A company appears in **200,000 articles**.

✅ Supported.

---

### Scenario 5

We decide to add **YouTube tech channels** later.

Could we?

Yes.

Just add another source.

No schema changes required.

---

# One Design Improvement I'd Like to Make

Most portfolio projects stop here.

I don't want ours to.

I'd like to add **two more tables** that make the project feel much more like something a real analytics company would build.

## 1. `scrape_jobs`

Instead of only logging individual scraper runs, this table tracks scheduled jobs.

```text
scrape_jobs

job_id
source_id
schedule_type
last_run
next_run
status
```

This becomes useful when we automate scraping daily or hourly.

## 2. `article_metrics`

Some values—like sentiment score, readability score, AI-generated summary quality, or topic classification—are **derived analytics**, not original article data.

Keeping them in a separate table has several advantages:

* You can rerun NLP models without modifying the original article.
* You preserve the distinction between **raw data** and **derived insights**.
* You can even compare results from different versions of your models later.

This separation is a common pattern in analytics platforms and gives us a cleaner architecture.

---

## Next Step

Now comes the part where we'll translate this design into SQL.

We'll create:

* `01_create_database.sql`
* `02_create_tables.sql`

But we won't just write `CREATE TABLE` statements—we'll discuss **data types, constraints, indexes, foreign keys, `ON DELETE` behavior, and why each choice matters**. That's where good database design really shines.


Excellent. Now we're entering what I call the **Database Architect** phase.

Most tutorials jump straight to:

```sql
CREATE TABLE articles(...)
```

We're **not** going to do that.

Instead, I'm going to teach you **how experienced database architects think**, because the SQL is actually the easy part.

---

# Before Writing SQL

Let's answer one question.

## What is the heart of our system?

Obviously,

> **Article**

Everything revolves around an article.

So the `articles` table will become our **fact table**.

Everything else is a dimension or lookup table.

This is actually similar to data warehouse thinking.

```
          Source
             |
Author ---- Article ---- Category
             |
        Companies
             |
       Technologies
             |
            Tags
```

Notice everything points toward the article.

---

# Step 1 — Choosing Primary Keys

Question:

Should we use

```
article_url
```

as Primary Key?

or

```
article_id
```

?

Many beginners choose

```
URL
```

because

> "Every URL is unique."

That's true...

until...

A news website changes its URL.

Now your Primary Key changes.

Primary Keys should **never change**.

So we'll use

```sql
article_id INT AUTO_INCREMENT PRIMARY KEY
```

The URL becomes

```sql
UNIQUE
```

instead.

---

We'll follow this for every table.

```
source_id

author_id

category_id

company_id

technology_id

tag_id
```

Everything gets a surrogate key.

---

# Step 2 — Data Types

Now comes something most people ignore.

Choosing the correct datatype.

For example

Title

Should we use

```
TEXT
```

or

```
VARCHAR
```

?

Let's think.

Average title

```
OpenAI launches GPT-6
```

Maybe

40 characters.

Longest?

Probably

200

Never thousands.

So

```
VARCHAR(300)
```

is perfect.

Not TEXT.

---

Now

Article Content

Average

1200 words.

Can easily exceed

10000 characters.

Here

TEXT

is appropriate.

---

Summary

Maybe

300 characters.

So

```
TEXT
```

or

```
VARCHAR(1000)
```

Either works.

I'd actually choose

```
TEXT
```

because different publishers have different summary lengths.

---

# URLs

```
https://techcrunch.com/2026/...
```

Maximum

around

200-300

characters.

But URLs can be surprisingly long.

Industry usually uses

```
VARCHAR(2048)
```

because that's a commonly accepted maximum URL length.

---

Publish Date

Never

VARCHAR

Never

TEXT

Always

```
DATETIME
```

or

```
TIMESTAMP
```

We'll discuss which shortly.

---

# Word Count

Maximum?

Maybe

15000

That's tiny.

```
INT
```

is enough.

---

Reading Time

```
6 min
```

Don't store

```
6 min
```

Store

```
6
```

as

```
SMALLINT
```

Presentation belongs in Tableau or Python.

---

# Step 3 — NULL vs NOT NULL

Another important design decision.

Should

Title

allow NULL?

No.

Every article has a title.

```
NOT NULL
```

---

Should

Content

allow NULL?

Maybe.

Sometimes RSS feeds don't provide the full article, or a scrape may fail after collecting metadata.

So

```
NULL
```

is acceptable.

---

Should

Published Date

allow NULL?

Again,

sometimes websites don't expose it.

We'll allow NULL.

---

Notice

Database design isn't about SQL.

It's about thinking.

---

# Step 4 — Constraints

Every table needs rules.

Example

Source Name

Should two sources have

```
TechCrunch
TechCrunch
```

twice?

No.

So

```
UNIQUE
```

---

URL

Two articles

Same URL?

Impossible.

```
UNIQUE
```

---

Category

```
AI
AI
AI
```

No.

```
UNIQUE
```

---

Company

```
Microsoft

Microsoft
```

Again

```
UNIQUE
```

---

These constraints protect your data quality.

---

# Step 5 — Indexing Strategy

This is where portfolio projects become impressive.

Ask yourself:

> What columns will I search frequently?

Probably

```
publish_date

source_id

category_id
```

Definitely.

We'll index them.

---

We'll search by

```
company
```

frequently.

Index.

---

Maybe

```
technology
```

Index.

---

Will we search by

```
summary
```

Often?

Probably not.

No index.

---

Indexes aren't free.

They speed up reads but slow down inserts because MySQL has to maintain the index.

So we index based on **query patterns**, not every column.

---

# Step 6 — Foreign Keys

Example

Article

belongs to

Source.

What happens if someone deletes

```
TechCrunch
```

?

Should all TechCrunch articles disappear?

Absolutely not.

Those articles are valuable historical data.

Instead,

MySQL should stop the deletion.

That's

```sql
ON DELETE RESTRICT
```

---

Now consider

Category.

Suppose

```
AI
```

gets renamed to

```
Artificial Intelligence
```

That's not a delete—it's an update.

We want related articles to reflect the new category automatically.

```sql
ON UPDATE CASCADE
```

---

# Step 7 — Choosing DATETIME vs TIMESTAMP

This is a subtle but important decision.

We actually have **two different kinds of time**:

### 1. When the article was published

Example:

```
2026-06-30 09:15
```

This date comes from the publisher.

It won't change.

We'll use:

```sql
published_at DATETIME
```

### 2. When **our system** scraped the article

Example:

```
2026-07-01 14:22
```

This is generated by our application.

We'll use:

```sql
scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

Why?

* `DATETIME` represents the article's own publication time.
* `TIMESTAMP` is ideal for system-generated events like inserts and updates.

---

# Our Design Principles

Before writing any SQL, we've established these rules:

* Every table gets a surrogate primary key (`AUTO_INCREMENT`).
* Business identifiers (like URLs) are protected with `UNIQUE`.
* Data types match the nature of the data.
* Constraints enforce data quality.
* Indexes are based on expected queries, not added everywhere.
* Foreign keys preserve referential integrity.
* We distinguish business timestamps from system timestamps.

---

## 🛑 I Don't Want to Rush the SQL

This may surprise you, but I **don't** want to start writing `CREATE TABLE` statements yet.

There's one more design artifact that professional teams create first: the **data dictionary**.

A data dictionary documents:

* Every table
* Every column
* Data type
* Constraints
* Description
* Business meaning

Once we have that, writing SQL becomes almost mechanical, and you'll have documentation that looks like it came from a real software or analytics team.

For a portfolio project, this is a huge differentiator. Most candidates show SQL scripts. Very few show the thought process and documentation behind the schema.

I recommend we spend one session building the data dictionary first, then implement the SQL immediately afterward. That will give you both a stronger project and a deeper understanding of every design decision.

Excellent. This is exactly how I wanted to build this project.

Most GitHub projects look like this:

```
project/
├── scraper.py
├── analysis.ipynb
└── dashboard.twb
```

A recruiter sees that and thinks:

> "This person knows some tools."

I want your repository to look like a project that was built by a small analytics team.

---

# What is a Data Dictionary?

A data dictionary is simply documentation of your database.

Think of it as the **instruction manual** for your database.

Suppose a new developer joins your team.

Instead of asking

> "What does `published_at` mean?"

they open the data dictionary.

Everything is documented.

Large companies like Google, Amazon, Microsoft, and banks maintain data dictionaries because databases can contain hundreds or thousands of columns.

---

# Our Data Dictionary

We'll create a file called

```
database/
    data_dictionary.md
```

Later we'll also create

```
database/

ERD.png

schema.sql

views.sql

indexes.sql

procedures.sql
```

---

# Let's Start with the Most Important Table

## Articles

This is our central entity.

Instead of jumping into SQL,

let's ask

> **What information should every article have?**

Here's my proposal.

| Column       | Data Type     | Constraints               | Why?                             |
| ------------ | ------------- | ------------------------- | -------------------------------- |
| article_id   | INT           | PK, AUTO_INCREMENT        | Internal unique identifier       |
| title        | VARCHAR(300)  | NOT NULL                  | Headline of the article          |
| url          | VARCHAR(2048) | UNIQUE, NOT NULL          | Original article URL             |
| summary      | TEXT          | NULL                      | Short description of the article |
| content      | LONGTEXT      | NULL                      | Full article body                |
| published_at | DATETIME      | NULL                      | When the article was published   |
| scraped_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP | When our scraper collected it    |
| word_count   | INT           | NULL                      | Number of words                  |
| reading_time | SMALLINT      | NULL                      | Estimated reading time (minutes) |
| category_id  | INT           | FK                        | Article category                 |
| source_id    | INT           | FK                        | News source                      |

---

## Let's Discuss Two Columns

### Why `LONGTEXT` instead of `TEXT`?

Many articles exceed **65,535 characters**, which is the limit of MySQL's `TEXT` type.

Approximate MySQL limits:

| Type       | Maximum Size |
| ---------- | -----------: |
| TINYTEXT   |    255 bytes |
| TEXT       |       ~64 KB |
| MEDIUMTEXT |       ~16 MB |
| LONGTEXT   |        ~4 GB |

We won't need 4 GB for an article, but using `LONGTEXT` guarantees we won't truncate content from long-form publications.

---

### Why `VARCHAR(2048)` for URLs?

Browsers generally support URLs up to around 2,048 characters.

Although most article URLs are much shorter, 2,048 is a widely accepted safe limit.

---

# Sources Table

Now let's think about the publishers.

| Column      | Type          | Constraints  | Why?                    |
| ----------- | ------------- | ------------ | ----------------------- |
| source_id   | INT           | PK           | Identifier              |
| source_name | VARCHAR(100)  | UNIQUE       | TechCrunch              |
| website     | VARCHAR(255)  | NOT NULL     | Home page               |
| rss_feed    | VARCHAR(2048) | NULL         | RSS URL                 |
| country     | VARCHAR(100)  | NULL         | Publisher country       |
| language    | VARCHAR(20)   | DEFAULT 'en' | Language                |
| active      | BOOLEAN       | DEFAULT TRUE | Enable/disable scraping |

---

Notice we didn't store:

```
Article Count

Latest Article

Average Reading Time
```

Why?

Because these are **derived values**.

The database should store facts.

Analytics should calculate metrics.

---

# Authors

Now comes our first interesting discussion.

Earlier I proposed a separate `authors` table.

However...

After thinking about the types of sources we plan to scrape, I'd like to revise the design.

### Why?

Many publishers don't have stable author IDs.

Some use:

```
John Doe
```

Others use:

```
John A. Doe
```

Some have:

```
Editorial Staff
```

Some don't list an author at all.

Also, author profile URLs aren't always available.

---

## My Proposal

Instead of

```
Authors

author_id
name
profile_url
bio
```

I'd prefer:

```
authors
------------
author_id
display_name
profile_url
```

And use a bridge table:

```
article_authors

article_id
author_id
```

This still supports:

* Multiple authors per article.
* Missing authors.
* Reused authors across many articles.

It's more flexible than storing `author_name` directly in `articles`.

---

# Categories

Simple lookup table.

| Column        | Type   |
| ------------- | ------ |
| category_id   | PK     |
| category_name | UNIQUE |

---

# Companies

| Column       | Type   |
| ------------ | ------ |
| company_id   | PK     |
| company_name | UNIQUE |

---

# Technologies

| Column          | Type   |
| --------------- | ------ |
| technology_id   | PK     |
| technology_name | UNIQUE |

---

# Tags

Exactly the same idea.

```
tag_id

tag_name
```

---

# Bridge Tables

Notice something.

Every bridge table has exactly two foreign keys.

Example

```
article_companies

article_id

company_id
```

No surrogate primary key.

Instead we'll make:

```
PRIMARY KEY(article_id, company_id)
```

This prevents duplicates automatically.

For example,

```
Article 10

OpenAI
```

cannot be inserted twice.

This is an excellent example of letting the database enforce data integrity.

---

# Scrape Logs

This table isn't about the news—it's about **our system**.

I propose:

| Column            | Purpose                    |
| ----------------- | -------------------------- |
| log_id            | Unique log ID              |
| source_id         | Which source was scraped   |
| started_at        | Start time                 |
| finished_at       | End time                   |
| articles_found    | Number discovered          |
| articles_inserted | Number stored              |
| status            | SUCCESS / FAILED / PARTIAL |
| error_message     | Failure details            |

This will help us debug and monitor the scraper.

---

# Here's a Design Question for You

I don't want this to become me making every decision. I want you to think like an architect too.

Suppose we scrape the same article again tomorrow.

Should we:

**Option A**

* Skip it entirely because the URL already exists.

**Option B**

* Update the existing article if the content has changed.

**Option C**

* Keep every version of the article as history.

There isn't one universally correct answer. Different companies choose different strategies depending on their business needs.

**What do you think we should do for TechPulse, and why?**

Your answer will influence the next part of our database design, because it determines whether we need versioning, update timestamps, or just deduplication. This is exactly the kind of trade-off that comes up in real data engineering projects.


