# TechTalent Insights — Global Tech Job Market Dashboard

An interactive Power BI dashboard analysing **1,500 tech job postings** across **12 countries** (2023–2024), exploring salary trends, in-demand skills, remote work patterns, and regional market differences.

Built as a hands-on Power BI portfolio project covering data modelling, DAX measures, and multi-page dashboard design.

---

## 📊 Dashboard Pages

### 1. Market Overview
- **1,500** total job postings across 12 countries
- **$136.8K** average salary (USD)
- Job distribution by country, remote type, employment type, and posting date
- Hybrid roles dominate at 45.2%, followed by Remote (30.2%) and On-site (24.6%)
- Full-time roles make up 70.7% of all postings

### 2. Salary Intelligence
- Average salary broken down by **role, experience level, country, and company size**
- Cloud Architects and ML Engineers command the highest salaries (~$180K+)
- Executive-level roles average 3x Entry-level compensation
- Enterprise companies offer ~30% higher salaries than startups
- Average benefits score: **3.75 / 5.0**

### 3. Skills in Demand
- **Python** is the most demanded skill globally (700+ mentions)
- **AWS** and **SQL** follow as the next most critical skills
- Full skills matrix: each country vs. every skill — showing regional demand differences
- Interactive slicer to filter by specific skill

### 4. Germany Deep Dive
- Germany vs. top 5 countries salary comparison (US, Switzerland, Netherlands, UK)
- Top German cities by average salary: Munich, Hamburg, Frankfurt, Berlin, Stuttgart
- Role distribution in Germany — Machine Learning Engineer leads skill demand
- Remote/hybrid/on-site split for German market specifically

---

## 🗂️ Dataset

Synthetic dataset modelled on real market patterns, generated with Python.

| File | Rows | Description |
|------|------|-------------|
| `jobs.csv` | 1,500 | Job postings — title, country, city, remote type, experience level, employment type |
| `salaries.csv` | 1,500 | Salary in USD and local currency, benefits score |
| `skills.csv` | 6,697 | One row per skill per job posting |
| `companies.csv` | 30 | Company reference data — size, industry, country |

---

## 🔗 Data Model

```
jobs (job_id) ──── salaries (job_id)   [one-to-one]
jobs (job_id) ──── skills (job_id)     [one-to-many]
```

---

## ⚙️ DAX Measures Used

```dax
Avg Salary USD = AVERAGE(salaries[salary_usd])

Total Jobs = COUNTROWS(jobs)

Skill Count = COUNTROWS(skills)

Germany Avg Salary = 
    CALCULATE([Avg Salary USD], jobs[country] = "Germany")

Remote Job % = 
    DIVIDE(
        CALCULATE(COUNTROWS(jobs), jobs[remote_type] = "Remote"),
        COUNTROWS(jobs)
    )
```

---

## 🛠️ Tools Used

- **Power BI Service** — report building and publishing
- **Power Query** — data cleaning and table relationships
- **DAX** — custom measures and filtered calculations
- **Python** — synthetic dataset generation (pandas, csv, random)

---

## 📁 Repository Structure

```
├── data/
│   ├── jobs.csv
│   ├── salaries.csv
│   ├── skills.csv
│   └── companies.csv
├── screenshots/
│   ├── 01_market_overview.png
│   ├── 02_salary_intelligence.png
│   ├── 03_skills_in_demand.png
│   └── 04_germany_deep_dive.png
├── generate_data.py
└── README.md
```

---

## 🚀 How to Reproduce

1. Clone the repo
2. Upload the 4 CSV files from `/data` to Power BI Service (or Power BI Desktop)
3. Build relationships: `jobs[job_id]` → `salaries[job_id]` and `skills[job_id]`
4. Create the DAX measures listed above
5. Build visuals as described in each dashboard page

To regenerate the dataset with a different random seed:
```bash
python generate_data.py
```

---

## 👤 Author

**Faraz Amjad** — Software Engineer & MSc student in Robotics and Autonomous Systems  
[farazamjad.de](https://farazamjad.de) · [LinkedIn](https://www.linkedin.com/in/farazamjad22) · [GitHub](https://github.com/farazamjad22)
