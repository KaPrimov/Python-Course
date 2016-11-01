
from demo.catalog import load_catalog
from demo.sales import load_sales, KEY_TS, KEY_PRICE, KEY_ITEM_ID, KEY_CITY

CATALOG_FILENAME = 'catalog.csv'
SALES_FILENAME = 'sales-10K.csv'


def main():
    catalog = load_catalog(CATALOG_FILENAME)
    sales = load_sales(SALES_FILENAME)
    print_total_stats()
    print_top_by_category(catalog)
    print_top_by_city()
    print_top_by_date(sales)


def print_total_stats():

    total_count = 0
    total_amount = 0
    min_timestamp = None
    max_timestamp = None

    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        total_amount += sale[KEY_PRICE]
        total_count += 1
        ts = sale[KEY_TS]

        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts
        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts

    print("""
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {avegage_price:.2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
""".format(
        total_count=total_count,
        total_amount=total_amount,
        avegage_price=total_amount / total_count if total_count else None,
        min_ts=min_timestamp,
        max_ts=max_timestamp,
    ))


def print_top_by_category(catalog):

    amounts_by_category = {}
    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_PRICE]
        category_name = catalog.get(item_id, None)

        if category_name not in amounts_by_category:
            amounts_by_category[category_name] = 0

        amounts_by_category[category_name] += price

    amounts_by_category_sorted = []

    amounts_by_category_sorted = list(amounts_by_category.items())
    amounts_by_category_sorted.sort(key=lambda kv: kv[1], reverse=True)

    print("""
Сума на продажби по категории (top 5)
-----------------------------
""")
    for category_name, total_amount in amounts_by_category_sorted[:5]:
        print("    {}: {:.2f} €".format(category_name, total_amount))


def print_top_by_city():
    amounts_by_city = {}
    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        city_name = sale[KEY_CITY]
        price = sale[KEY_PRICE]

        if city_name not in amounts_by_city:
            amounts_by_city[city_name] = 0
        amounts_by_city[city_name] += price

    amounts_by_city_sorted = []
    for city_name, total_amount in amounts_by_city.items():
        amounts_by_city_sorted.append((total_amount, city_name))

    amounts_by_city_sorted.sort(reverse=True)

    print("""
Сума на продажби по градове (top 5)
-----------------------------""")
    for total_amount, city_name in amounts_by_city_sorted[:5]:
        print("    {}: {:.2f} €".format(city_name, total_amount))


def print_top_by_date(sales: list):

    amounts_by_date = {}
    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        date = sale[KEY_TS].replace(minute=0, second=0)
        price = sale[KEY_PRICE]

        if date not in amounts_by_date:
            amounts_by_date[date] = 0
        amounts_by_date[date] += price
    amounts_by_date_sorted = []

    amounts_by_date_sorted = list(amounts_by_date.items())
    amounts_by_date_sorted.sort(key=lambda kv: kv[1], reverse=True)


    print("""
Сума на продажби по час (top 5)
-----------------------------""")
    for date, total_amount in amounts_by_date_sorted[:5]:
        print("    {}: {:.2f} €".format(date, total_amount))


if __name__ == '__main__':
    main()
