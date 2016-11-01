from analyzers import *
from catalog import load_catalog
from sales import load_sales

CATALOG_FILENAME = 'catalog.csv'
SALES_FILENAME = 'sales-10K.csv'


def main():
    catalog = load_catalog(CATALOG_FILENAME)

    analyzers = [
        TotalsAnalyzer(),
        AmountsByCategoryAnalyzer(catalog),
        AmountsByCityAnalyzer(catalog),
        AmountsByHourAnalyzer(catalog),
    ]

    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        for a in analyzers:
            a.analyze_sale(sale)

    for a in analyzers:
        a.print_results()


if __name__ == '__main__':
    main()