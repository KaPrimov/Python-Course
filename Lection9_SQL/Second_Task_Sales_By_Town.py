import sqlite3
import csv
import iso8601

DB_FILENAME = 'sales-database.db'
CATALOG_FILENAME = 'catalog.csv'
SALES_FILENAME = 'sales-10K.csv'

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'


def main():
    city = input("Въведете име на град: ")
    print("Продажби в град {}:".format(city))
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:
        filter_sales_by_city(connection, SALES_FILENAME, city)


def load_sales(filename: str) -> list:

    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = {}
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TS])
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            result.append(sale)
    return result


def filter_sales_by_city(connection, sales_filename, city):
    sales = load_sales(sales_filename)
    cursor = connection.cursor()
    for sale in sales:
        sale_timestamp = sale[KEY_TS]
        cursor.execute(
            'select * from sale order by sale_timestamp asc'
        )
        if city == sale[KEY_CITY]:
            print("Артикул #: {}   дата/час: {}   сума: {}"
                  .format(sale[KEY_ITEM_ID], sale[KEY_TS], sale[KEY_PRICE]))

if __name__ == '__main__':
    main()
