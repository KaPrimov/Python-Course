import sqlite3


def main():
    with sqlite3.connect('./sales-example.db', isolation_level=None) as connection:
        print_catalog(connection)
        # demo_sql_injection(connection)
        new_catalog_entry(connection, item_key='11111111', category='OIUIUYUYT')
        print_catalog(connection)


def demo_sql_injection(connection):
    """

    !!!!!!!!! DO NOT DO THIS !!!!!!!!!

    :param connection:
    :return:
    """
    print('DEMO: SQL Injection')
    username = input("username: ")
    password = '28542932652237584905972396438992379dfvdhcdjvhgbh'
    wrong_sql_auth = "select * from users where username='" + username + "' and password='{}';".format(username, password)
    print(wrong_sql_auth)

    # item_key = input("item id = ")
    # category = 'jyftguhj'
    #  wrong_sql = "insert into catalog (item_key, category) values ('{}', '{}')".format(item_key, category)
    # print(wrong_sql)


def new_catalog_entry(connection, item_key: str, category: str):
    """
    insert into catalog (item_key, category) values ('888888', 'BALLS');
    """
    cursor = connection.cursor()
    cursor.execute(
        'insert into catalog (item_key, category) values (?, ?)',
        [item_key, category]
    )


def print_catalog(connection):
    cursor = connection.cursor()
    cursor.execute('select * from catalog')
    for row_number, row in enumerate(cursor.fetchall(), start=1):
        print("\nRecord #{}".format(row_number))
        print("\tid = {}".format(row[0]))
        print("\titem_key = {}".format(row[1]))
        print("\tcategory = {}".format(row[2]))


if __name__ == '__main__':
    main()