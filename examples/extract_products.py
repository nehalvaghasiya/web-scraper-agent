from pydantic import BaseModel, Field
from typing import List
from scraper import scrape


class Product(BaseModel):
    brand: str = Field(..., description="Brand name")
    name: str = Field(..., description="Product name")
    price: str | None
    stars: float | None
    reviews: int | None


class Results(BaseModel):
    products: List[Product]


# URL from which we want to extract the list of product information
URL = "https://www.amazon.de/wireless-headphones/s?k=wireless+headphones"

prompt_template = """
Extract a list of products from the following Amazon page text.

Return in JSON format:
{{
  "products": [
    {{
      "brand": "Brand name",
      "name": "Full product title",
      "price": "EUR 59.99",
      "stars": 4.5,
      "reviews": 1223
    }}
  ]
}}

HTML:
{html}
"""

data = scrape(URL, prompt_template, Results)
print(data)
# Expected output:
# products=[
#     Product(brand='CASCHO', name='Bluetooth sports headphones – 60 hours', price='€28.79', stars=None, reviews=None),
#     Product(brand='', name='Bluetooth Headphones, Wireless Bluetooth 5.4, In-Ear Headphones with ENC Noise Cancelling Mics, IP7 Waterproof Earphones with HiFi Stereo, 50 Hours Playtime, Wireless Headphones, USB-C LED Display', price='€24.99', stars=4.9, reviews=276),
#     Product(brand='', name='Bluetooth Headphones, Wireless, Bluetooth 5.3 In-Ear Headphones, with 4 Microphones, ENC Noise Reduction Earphones, 40 Hours, Deep Bass', price='€26.59', stars=4.4, reviews=50653),
#     Product(brand='soundcore by Anker', name='P20i Wireless Bluetooth Headphones In-Ear, 10 mm Driver, Bluetooth 5.3, Adjustable EQ, 30 Hours Playtime, IPX5 Waterproof, 2 Micros with AI, Single Use (Black)', price='€24.99', stars=4.4, reviews=62500),
#     Product(brand='Sony', name='WH-CH520 Wireless Bluetooth Headphones - Up to 50 Hours Battery Life with Quick Charge Function, On-Ear Model - Black', price='€32.99', stars=4.5, reviews=29694),
#     Product(brand='soundcore by Anker', name='Q20i Wireless Bluetooth Over-Ear Headphones with Hybrid Active Noise Cancelling, 40h Playtime in ANC Mode, Hi-Res Audio, Deep Bass, Personalization via App (Black)', price='€29.99', stars=4.6, reviews=31020)
# ]

