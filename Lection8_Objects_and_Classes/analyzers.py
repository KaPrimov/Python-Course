from sales import KEY_PRICE, KEY_TS, KEY_ITEM_ID, KEY_CITY


class BaseAnalyzer:

    def analyze_sale(self, sale):
        ...

    def print_results(self):
        ...


class TotalsAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()
        self.total_count = 0
        self.total_amount = 0
        self.min_timestamp = None
        self.max_timestamp = None

    def analyze_sale(self, sale):
        self.total_amount += sale[KEY_PRICE]
        self.total_count += 1

        ts = sale[KEY_TS]
        if self.min_timestamp is None or ts < self.min_timestamp:
            self.min_timestamp = ts
        if self.max_timestamp is None or ts > self.max_timestamp:
            self.max_timestamp = ts

    def print_results(self):
        print("""
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {avegage_price:.2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
    """.format(
            total_count=self.total_count,
            total_amount=self.total_amount,
            avegage_price=self.total_amount / self.total_count if self.total_count else None,
            min_ts=self.min_timestamp,
            max_ts=self.max_timestamp,
        ))


class AmountsGroupedAnalyzer(BaseAnalyzer):
    group_by_title = ''

    def __init__(self, catalog ):
        super().__init__()
        self.amounts_grouped = {}  # key : category name  ,  value : accumulated sum of sales
        self.catalog = catalog

    def analyze_sale(self, sale):
        price = sale[KEY_PRICE]
        group_by_value = self.get_group_by_value(sale)
        if group_by_value not in self.amounts_grouped:
            self.amounts_grouped[group_by_value] = 0
        self.amounts_grouped[group_by_value] += price

    def get_group_by_value(self, sale):
        ...

    def print_results(self):
        # [ (category1, sales_amount1), (category2, sales_amount2),...]
        amounts_grouped_sorted = list(self.amounts_grouped.items())
        amounts_grouped_sorted.sort(key=lambda kv: kv[1], reverse=True)

        print("""
Сума на продажби по {} (top 5)
-----------------------------
    """.format(self.group_by_title))
        for category_name, total_amount in amounts_grouped_sorted[:5]:
            print("     {}: {:.2f} €".format(category_name, total_amount))


class AmountsByCategoryAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = 'категории'

    def get_group_by_value(self, sale):
        # item_id = sale[KEY_ITEM_ID]
        return self.catalog.get(KEY_ITEM_ID, None)


class AmountsByCityAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = 'градове'

    def get_group_by_value(self, sale):
        return sale[KEY_CITY]


class AmountsByHourAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = 'часове'

    def get_group_by_value(self, sale):
        ts = sale[KEY_TS]
        ts = ts.replace(minute=0, second=0, microsecond=0)
        return ts