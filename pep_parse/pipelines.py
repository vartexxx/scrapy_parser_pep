import csv
import datetime as dt

from itemadapter import ItemAdapter

from .exceptions import NoStatusException
from .settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def __init__(self):
        self.pep_status = None
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.pep_status = {}

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            pep_status = adapter['status']
            self.pep_status[pep_status] = (
                    self.pep_status.get(pep_status, 0) + 1)
            return item
        else:
            raise NoStatusException(f'missing status: {item}')

    def close_spider(self, spider):
        total = spider.crawler.stats.get_stats()['item_scraped_count']
        time_formated = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{time_formated}.csv'
        file_path = self.results_dir / file_name
        writing_format = (
                [['Статус', 'Количество']] + [[k, v] for k, v in self.pep_status.items()]
                +
                [['Total', total]]
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(writing_format)
