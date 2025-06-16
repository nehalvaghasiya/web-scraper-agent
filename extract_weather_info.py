from pydantic import BaseModel, Field
from typing import List
from scraper import scrape


class ForecastEntry(BaseModel):
    day: str
    high_c: float = Field(description="High temp in Celsius")
    low_c: float = Field(description="Low temp in Celsius")
    chance_of_rain: int = Field(description="Chance of rain in percent")


class CityForecast(BaseModel):
    city: str
    entries: List[ForecastEntry]


class MultiCityForecasts(BaseModel):
    forecasts: List[CityForecast]


weather_prompt = """
From the HTML of a weather forecast website that includes forecasts for **multiple cities**, extract a list of 10-day forecasts for each city.

Return a JSON like this:

{{
  "forecasts": [
    {{
      "city": "Berlin",
      "entries": [
        {{
          "day": "Monday",
          "high_c": 28.0,
          "low_c": 17.5,
          "chance_of_rain": 60
        }},
        ...
      ]
    }},
    {{
      "city": "Paris",
      "entries": [
        {{
          "day": "Monday",
          "high_c": 25.0,
          "low_c": 16.0,
          "chance_of_rain": 50
        }},
        ...
      ]
    }}
  ]
}}

Each city's forecast should include exactly 10 days if available.

HTML:
{html}
"""

URL = "https://www.timeanddate.com/weather/germany"  # Use a page that lists forecasts for multiple cities
data = scrape(URL, weather_prompt, MultiCityForecasts)
print(data)

# ✅ Expected output format:
# forecasts = [
#     CityForecast(
#         city="Berlin",
#         entries=[
#             ForecastEntry(day="Saturday", high_c=22.0, low_c=12.0, chance_of_rain=60),
#             ForecastEntry(day="Sunday", high_c=25.0, low_c=15.0, chance_of_rain=30),
#             ...
#         ]
#     ),
#     CityForecast(
#         city="Munich",
#         entries=[
#             ForecastEntry(day="Saturday", high_c=24.0, low_c=14.0, chance_of_rain=50),
#             ForecastEntry(day="Sunday", high_c=26.0, low_c=15.0, chance_of_rain=20),
#             ...
#         ]
#     )
# ]
