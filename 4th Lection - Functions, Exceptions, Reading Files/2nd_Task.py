import csv

FILE_NAME = "catalog_full.csv"
COLUMN_NAMES = ('cat_number', 'product_name', 'product_colour', 'purpose', 'product_group', 'sex', 'price' )

with open(FILE_NAME, 'r', encoding='UTF-8') as infile:
    infile_csv = csv.reader(infile, delimiter=',')

    prices_sums = {}
    prices_counts = {}

    for row_num, row in enumerate(infile_csv):
        mapped_row = dict(zip(COLUMN_NAMES, row))
        product_sex = mapped_row['sex']
        product_prices = mapped_row['price']

        try:
            prices_sums[product_sex] = prices_sums[product_sex] + float(product_prices)
            prices_counts[product_sex] += 1
        except:
            prices_sums[product_sex] = float(product_prices)
            prices_counts[product_sex] = 1

    for sex in prices_sums.keys():
        prices_sum = prices_sums[sex]
        product_count = prices_counts[sex]
        average_price = prices_sum/product_count

        print('Average price of {0}\'s products: {1:.2f}'.format(sex, average_price))

