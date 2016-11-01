import csv

CATALOG_FILENAME = 'catalog.csv'

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5


def load_catalog(filename: str) -> dict:

    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category
    return result

