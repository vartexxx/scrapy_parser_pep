import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_NAME_PATTERN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        peps = response.xpath(
            '//section[@id="numerical-index"]'
        ).xpath(
            './/a[@class="pep reference internal"]/@href'
        )
        for link in peps:
            yield response.follow(link, callback=self.parse_pep)

    @staticmethod
    def parse_pep(response):
        number, name = re.search(
            PEP_NAME_PATTERN,
            response.css('h1.page-title::text').get()
        ).groups()
        yield PepParseItem({
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get()
        })
