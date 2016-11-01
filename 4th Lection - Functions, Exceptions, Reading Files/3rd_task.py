def changing_prices_in_catalog(filename_to_read_from, filename_to_write_in):
    with open(filename_to_read_from, 'r', encoding='utf-8') as f_old_prices:
         with open(filename_to_write_in, 'w', encoding='utf-8') as f_new_prices:
             for line in f_old_prices:
                 stripped_line = line.strip()
                 list_of_the_line = stripped_line.split()
                 list_of_the_line[6] = 175/100 * float(list_of_the_line[6])
                 list_of_the_line[6] = str(list_of_the_line[6])
                 f_new_prices.write(','.join(list_of_the_line))
                 f_new_prices.write('\n')

changing_prices_in_catalog('catalog_fill', 'new_file')
