import csv
import random
from datetime import datetime, timedelta

random.seed(42)

countries = {
    "Germany": {"cities": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Stuttgart"], "currency": "EUR", "multiplier": 0.85},
    "United States": {"cities": ["San Francisco", "New York", "Seattle", "Austin", "Boston"], "currency": "USD", "multiplier": 1.0},
    "United Kingdom": {"cities": ["London", "Manchester", "Edinburgh", "Bristol"], "currency": "GBP", "multiplier": 0.78},
    "Netherlands": {"cities": ["Amsterdam", "Rotterdam", "Utrecht"], "currency": "EUR", "multiplier": 0.82},
    "France": {"cities": ["Paris", "Lyon", "Toulouse"], "currency": "EUR", "multiplier": 0.78},
    "Canada": {"cities": ["Toronto", "Vancouver", "Montreal"], "currency": "CAD", "multiplier": 0.74},
    "Switzerland": {"cities": ["Zurich", "Geneva", "Basel"], "currency": "CHF", "multiplier": 0.92},
    "Australia": {"cities": ["Sydney", "Melbourne", "Brisbane"], "currency": "AUD", "multiplier": 0.65},
    "India": {"cities": ["Bangalore", "Hyderabad", "Pune", "Mumbai"], "currency": "USD", "multiplier": 0.28},
    "Poland": {"cities": ["Warsaw", "Krakow", "Wroclaw"], "currency": "EUR", "multiplier": 0.52},
    "Spain": {"cities": ["Madrid", "Barcelona", "Valencia"], "currency": "EUR", "multiplier": 0.68},
    "Sweden": {"cities": ["Stockholm", "Gothenburg"], "currency": "EUR", "multiplier": 0.80},
}

roles = {
    "Software Engineer": {"base": 95000, "skills": ["Python", "Java", "Git", "Docker", "SQL", "AWS", "Kubernetes", "React"]},
    "Data Engineer": {"base": 100000, "skills": ["Python", "SQL", "Spark", "Airflow", "dbt", "AWS", "Kafka", "Snowflake"]},
    "Data Analyst": {"base": 78000, "skills": ["SQL", "Python", "Power BI", "Excel", "Tableau", "Statistics", "R"]},
    "Machine Learning Engineer": {"base": 120000, "skills": ["Python", "TensorFlow", "PyTorch", "SQL", "Docker", "AWS", "Scikit-learn"]},
    "iOS Developer": {"base": 92000, "skills": ["Swift", "SwiftUI", "UIKit", "Xcode", "Git", "REST APIs", "Agile"]},
    "Backend Engineer": {"base": 98000, "skills": ["Python", "Java", "Go", "PostgreSQL", "Docker", "AWS", "Redis", "Kafka"]},
    "Frontend Engineer": {"base": 88000, "skills": ["JavaScript", "TypeScript", "React", "Vue.js", "CSS", "Git", "GraphQL"]},
    "DevOps Engineer": {"base": 105000, "skills": ["Docker", "Kubernetes", "AWS", "Terraform", "CI/CD", "Linux", "Python"]},
    "Product Manager": {"base": 110000, "skills": ["Agile", "SQL", "Jira", "Product Strategy", "Analytics", "Roadmapping"]},
    "Business Intelligence Analyst": {"base": 82000, "skills": ["Power BI", "SQL", "Excel", "DAX", "Qlik", "Tableau", "Python"]},
    "Cloud Architect": {"base": 130000, "skills": ["AWS", "Azure", "GCP", "Terraform", "Docker", "Kubernetes", "Networking"]},
    "Security Engineer": {"base": 115000, "skills": ["Python", "Network Security", "AWS", "Penetration Testing", "Linux", "SIEM"]},
}

experience_levels = {"Entry": 0.70, "Mid": 1.0, "Senior": 1.40, "Lead": 1.65, "Executive": 2.0}
company_sizes = {"Startup (1-50)": 0.88, "Small (51-200)": 0.93, "Medium (201-1000)": 1.0, "Large (1001-5000)": 1.08, "Enterprise (5000+)": 1.15}
remote_types = ["Remote", "Hybrid", "On-site"]
remote_weights = [0.30, 0.45, 0.25]
industries = ["FinTech", "HealthTech", "E-Commerce", "SaaS", "Automotive", "Consulting", "Gaming", "Logistics", "EdTech", "Cybersecurity"]
employment_types = ["Full-time", "Part-time", "Contract", "Working Student"]
employment_weights = [0.70, 0.05, 0.15, 0.10]

# ── jobs.csv ──────────────────────────────────────────────────
jobs = []
start_date = datetime(2023, 1, 1)
for job_id in range(1, 1501):
    country = random.choice(list(countries.keys()))
    city = random.choice(countries[country]["cities"])
    role = random.choice(list(roles.keys()))
    exp = random.choice(list(experience_levels.keys()))
    size = random.choice(list(company_sizes.keys()))
    remote = random.choices(remote_types, weights=remote_weights)[0]
    emp_type = random.choices(employment_types, weights=employment_weights)[0]
    industry = random.choice(industries)
    date_posted = start_date + timedelta(days=random.randint(0, 730))
    jobs.append({
        "job_id": job_id,
        "title": role,
        "company_size": size,
        "industry": industry,
        "country": country,
        "city": city,
        "remote_type": remote,
        "employment_type": emp_type,
        "experience_level": exp,
        "date_posted": date_posted.strftime("%Y-%m-%d"),
    })

with open("/home/claude/jobs.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=jobs[0].keys())
    w.writeheader(); w.writerows(jobs)

# ── salaries.csv ──────────────────────────────────────────────
salaries = []
for job in jobs:
    base = roles[job["title"]]["base"]
    exp_mult = experience_levels[job["experience_level"]]
    size_mult = company_sizes[job["company_size"]]
    country_mult = countries[job["country"]]["multiplier"]
    currency = countries[job["country"]]["currency"]
    noise = random.uniform(0.88, 1.12)
    salary_usd = round(base * exp_mult * size_mult * noise)
    salary_local = round(salary_usd * country_mult)
    benefits = round(random.uniform(2.5, 5.0), 1)
    salaries.append({
        "job_id": job["job_id"],
        "salary_usd": salary_usd,
        "salary_local": salary_local,
        "currency": currency,
        "benefits_score": benefits,
    })

with open("/home/claude/salaries.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=salaries[0].keys())
    w.writeheader(); w.writerows(salaries)

# ── skills.csv ────────────────────────────────────────────────
skills_rows = []
skill_id = 1
for job in jobs:
    role_skills = roles[job["title"]]["skills"]
    n = random.randint(3, 6)
    chosen = random.sample(role_skills, min(n, len(role_skills)))
    for skill in chosen:
        skills_rows.append({"skill_id": skill_id, "job_id": job["job_id"], "skill": skill})
        skill_id += 1

with open("/home/claude/skills.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["skill_id", "job_id", "skill"])
    w.writeheader(); w.writerows(skills_rows)

# ── companies.csv ─────────────────────────────────────────────
company_names = [
    "DataFlow GmbH", "TechBridge AG", "NexaCloud", "PulseAI", "StackMind",
    "Orion Systems", "BluePath Labs", "Vertex Technologies", "Momentum Digital",
    "CoreSync", "Helios Software", "Quantum Leap GmbH", "GridLogic", "Nimbus Tech",
    "Axiom Analytics", "DeepRoot", "Horizon Engineering", "Lumen Data", "Sparq GmbH",
    "Ironclad Solutions", "Wavefront AI", "Prism Technologies", "Atlas Digital",
    "Beacon Analytics", "Cipher Labs", "Drift Systems", "Echo Technologies",
    "Forge Digital", "Gravity Solutions", "Harbor Tech"
]
companies = []
for i, name in enumerate(company_names, 1):
    country = random.choice(list(countries.keys()))
    size = random.choice(list(company_sizes.keys()))
    industry = random.choice(industries)
    founded = random.randint(2000, 2022)
    companies.append({"company_id": i, "name": name, "industry": industry,
                       "country": country, "size": size, "founded_year": founded})

with open("/home/claude/companies.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=companies[0].keys())
    w.writeheader(); w.writerows(companies)

# ── summary ───────────────────────────────────────────────────
print(f"jobs.csv        → {len(jobs)} rows")
print(f"salaries.csv    → {len(salaries)} rows")
print(f"skills.csv      → {len(skills_rows)} rows")
print(f"companies.csv   → {len(companies)} rows")
