class BaseAnalyzer:
    def analyze_sale(self):
        ...

    def print_results(self):
        ...


class TotalsAnalyzer(BaseAnalyzer):

    def __init__(self):
        self.total_count = 0
        self.total_amount = 0
        self.min_timestamp = None
        self.max_timestamp = None


    def analyze_sale(self):
        total_amount += sale[KEY_PRICE]
#         total_count += 1
#         ts = sale[KEY_TS]
#
#         if min_timestamp is None or ts < min_timestamp:
#             min_timestamp = ts
#         if max_timestamp is None or ts > max_timestamp:
#             max_timestamp = ts...
    def print_results(self):
        ...