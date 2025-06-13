from pydantic import BaseModel, Field
from typing import List
from scraper import scrape


class Post(BaseModel):
    title: str
    author: str | None
    published: str | None = Field(description="ISO date")
    summary: str

class BlogFeed(BaseModel):
    posts: List[Post]

blog_prompt = """
From the HTML text of a blog or news front-page, extract the list of recent blog posts.

Return a JSON in this format:

{{
  "posts": [
    {{
      "title": "Post title",
      "author": "Author name or None",
      "published": "2024-05-06" or null,
      "summary": "Brief summary of the post"
    }},
    ...
  ]
}}

HTML:
{html}
"""
URL = "https://techcrunch.com/"
data = scrape(URL, blog_prompt, BlogFeed)
print(data)
# ✅ This should be the expected output format:
# posts = [
#     Post(
#         title="Zevo’s EV-only car-share fleet is helping Tesla owners make money",
#         author="Sean O'Kane",
#         published=None,
#         summary="Zevo’s EV-only car-share fleet is helping Tesla owners make money"
#     ),
#     Post(
#         title="Amazon joins the big nuclear party, buying1.92 GW for AWS",
#         author="Tim De Chant",
#         published=None,
#         summary="Amazon joins the big nuclear party, buying1.92 GW for AWS"
#     ),
#     Post(
#         title="Apple’s Liquid Glass design is paving the way for AR glasses",
#         author="Amanda Silberling",
#         published=None,
#         summary="Apple’s Liquid Glass design is paving the way for AR glasses"
#     ),
#     Post(
#         title="Silicon Valley tech execs are joining the US Army Reserve",
#         author="Rebecca Szkutak",
#         published=None,
#         summary="Silicon Valley tech execs are joining the US Army Reserve"
#     ),
#     Post(
#         title="Clay secures a new round at a $3B valuation, sources say",
#         author="Marina Temkin",
#         published=None,
#         summary="Clay secures a new round at a $3B valuation, sources say"
#     ),
#     Post(
#         title="Google tests Audio Overviews for Search queries",
#         author="Aisha Malik",
#         published=None,
#         summary="Google tests Audio Overviews for Search queries"
#     ),
#     Post(
#         title="Startups Weekly: No sign of pause",
#         author="Anna Heim",
#         published=None,
#         summary="Startups Weekly: No sign of pause"
#     ),
#     Post(
#         title="Beyond Bluesky: These are the apps building social experiences on the AT Protocol",
#         author="Sarah Perez",
#         published=None,
#         summary="Beyond Bluesky: These are the apps building social experiences on the AT Protocol"
#     )
# ]


