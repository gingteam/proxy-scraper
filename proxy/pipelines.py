# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from proxy.items import ProxyItem


class ProxyPipeline:
    def process_item(self, item: ProxyItem, spider):
        with open('proxies.txt', 'a') as file:
            file.write(f'{item["type"]}://{item["ip"]}:{item["port"]}\n')

        return item
