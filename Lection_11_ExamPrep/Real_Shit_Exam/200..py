import pprint
import csv

try:
    def main():
        filename = input()
        if filename == '':
            print("INVALID INPUT")
        else:
            standings = load_packages(filename)
            if standings:
                result_per_country = {}
                for standing in standings:
                    country, medal = standing
                    if country not in result_per_country:
                        result_per_country[country] = medal
                    else:
                        result_per_country[country] += medal
                top_results = list(result_per_country.items())
                top_results.sort(key=lambda n: n[0], reverse=True)
                top_results.sort(key=lambda m: m[1], reverse=True)
                for result in top_results:
                    print(result[0])


    def load_packages(fn: str) -> list:
        result = []
        with open(fn, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                medal = row[2]
                if medal == 'gold':
                    medal = int(7)
                elif medal == 'silver':
                    medal = int(3)
                elif medal == 'bronze':
                    medal = int(1)
                country = row[3]

                result.append((country, medal))

        return result

    if __name__ == '__main__':
        main()
except:
    print("INVALID INPUT")
