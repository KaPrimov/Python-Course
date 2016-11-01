FIELD_START_URL = 'url="'
FIELD_START_URL_LEN = len(FIELD_START_URL)

FIELD_START_RESPONSE_TIME = 'resp_t="'
FIELD_START_RESPONSE_TIME_LEN = len(FIELD_START_RESPONSE_TIME)
FIELD_END = '"'
PARAMS_SEP = '?'
IGNORE_SUFFIX = 'ws/'

def main():

    try:
        data_filename = input()

        max_times_per_url = {}

        sum_times_per_url = {}
        counts_per_url = {}

        with open(data_filename, encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    url = extract_field(line, FIELD_START_URL)
                    params_pos = url.find(PARAMS_SEP)
                    if params_pos >= 0:
                        url = url[:params_pos]

                    if url.endswith(IGNORE_SUFFIX):
                        continue

                    response_time = extract_field(line, FIELD_START_RESPONSE_TIME)
                    response_time = float(response_time)

                    if url not in sum_times_per_url:
                        sum_times_per_url[url] = 0
                        counts_per_url[url] = 0
                    sum_times_per_url[url] += response_time
                    counts_per_url[url] += 1

        if sum_times_per_url:
            max_avg_times = []
            for url in sum_times_per_url:
                avg_time = sum_times_per_url[url] / counts_per_url[url]
                max_avg_times.append((avg_time, url))

            max_time = max(max_avg_times)
            print(max_time[1])
            print("{:.3f}".format(max_time[0]))
        else:
            print("NO ITEMS")

    except Exception as e:
        print("INVALID INPUT")
        print(e)


def extract_field(line, field_start: str, field_end: str=FIELD_END) -> str:
    field_start_len = len(field_start)

    field_pos = line.find(field_start)
    if field_pos == -1:
        raise ValueError("No URL field found")

    return line[field_pos+field_start_len:line.find(field_end, field_pos+field_start_len)]

if __name__ == '__main__':
    main()