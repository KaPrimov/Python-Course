import csv


def main():
    item_id = input()
    sales_fn = input()

    sales = load_sales(sales_fn)
    if sales:
        min_price_city_per_item = {}
        for sale in sales:
            sale_item_id, city_name, price = sale
            if sale[0] != item_id:
                continue
            if city_name not in min_price_city_per_item:
                min_price_city_per_item[city_name] = price
            else:
                if price < min_price_city_per_item[city_name]:
                    min_price_city_per_item[city_name] = price

        min_prices = list(min_price_city_per_item.items())
        min_prices.sort(key=lambda i: i[1])
        print(min_prices[0][0])
    else:
        print("INVALID INPUT")


    # shorter solution
    #     sales_filtered = list(filter(lambda sale: sale[0] == item_id, sales))
    #     min_sale = min(sales_filtered, key=lambda sale: sale[2])
    #     print(min_sale[1])
    # except:
    #     print("INVALID INPUT")


def load_sales(fn: str) -> list:
    result=[]
    with open(fn, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if len(row) != 5:
                raise Exception("INVALID ROW")

            item_id = row[0]
            city_name = row[2]
            price = float(row[-1])

            result.append(
                (item_id, city_name, price)
            )
    return result


if __name__ == '__main__':
    main()