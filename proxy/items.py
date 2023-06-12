# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from typing import TypedDict


class ProxyItem(TypedDict):
    ip: str
    port: int
    type: str
