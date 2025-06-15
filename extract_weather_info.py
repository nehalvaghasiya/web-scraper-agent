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