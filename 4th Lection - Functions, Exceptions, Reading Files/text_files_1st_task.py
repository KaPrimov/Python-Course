full_catalogue = []

with open('catalog_sample.csv', encoding='utf-8') as f:
    for line in f:
        line.strip()
        line = line.split(',')
        full_catalogue.append(line)

avg_sum = 0
for i in full_catalogue:
    avg_sum += float(i[-1])
avg_sum /= len(full_catalogue)
print(avg_sum)
