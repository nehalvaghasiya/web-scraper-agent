from typing import List

from pydantic import BaseModel

from scraper import scrape


class Job(BaseModel):
    title: str
    company: str
    location: str | None
    posted: str | None
    description_snippet: str | None


class JobResults(BaseModel):
    jobs: List[Job]


job_prompt = """
Extract job listings from the given job board HTML.

Return JSON in this format:

{{
  "jobs": [
    {{
      "title": "Job title",
      "company": "Company name",
      "location": "City or Region",
      "posted": "Posted date or relative time (e.g. '3 days ago')",
      "description_snippet": "Short preview of the job description"
    }},
    ...
  ]
}}

HTML:
{html}
"""

URL = "https://www.linkedin.com/jobs/data-analyst-jobs-germany"
data = scrape(URL, job_prompt, JobResults)
print(data)
# Expected output:
# jobs = [
#     Job(title='Data Analyst', company='PUMA Group', location='Herzogenaurach, Bavaria, Germany', posted='1 day ago', description_snippet=None),
#     Job(title='Data Analyst (Payment, Fintech)', company='Delivery Hero', location='Berlin, Berlin, Germany', posted='1 week ago', description_snippet=None),
#     Job(title='Data Analyst (m/f/d)', company='atmio', location='Berlin, Berlin, Germany', posted='2 weeks ago', description_snippet=None)
# ]
