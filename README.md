# Асинхронный парсер PEP

## Парсинг документации PEP  с помощью Scrapy
> Парсер документов PEP на базе фреймворка Scrapy создает два файла отчета: файл со списком PEP, включающим номер документа, название и статус, и файл суммарной статистики по количеству документов в разных статусах.

## Стек технологий:
- Python
- Scrapy


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/vartexxx/scrapy_parser_pep.git

cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv

. venv/bin/activate
```

Обновить пакетный менеджер и установить зависимости:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

## Список поддерживаемых комманд:
Запуск парсера из виртуального окружения:
```
scrapy crawl pep
```

### Автор
Бурлака Владислав
vartexxx29@yandex.ru