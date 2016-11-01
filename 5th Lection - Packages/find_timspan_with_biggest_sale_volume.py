from datetime import datetime
import iso8601
import operator

sales_count_by_hour = {}

# dt = datetime.now()

for dt in sales_by_hour:
    dt = dt.replace(minute=0, second=0, microsecond=0)
    dt_parsed = iso8601.parse_date(dt)
    if dt not in sales_count_by_hour:
        sales_count_by_hour[dt_parsed] = 1
    else:
        sales_count_by_hour[dt_parsed] += 1

def GetMaxFlox(flows):
    return max((len(v), v, k) for k, v in flows.iteritems())[1:]

GetMaxFlox(sales_count_by_hour)