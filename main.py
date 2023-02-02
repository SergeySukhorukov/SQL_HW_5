import psycopg2
import sql_func
import os
conn = psycopg2.connect(database="user_db", user="postgres", password="postgres")
with conn.cursor() as cur:
    print("""Какую операцию вы хотите выполнить? 
1 - Функция, создающая структуру БД (таблицы)
2 - Функция, позволяющая добавить нового клиента
3 - Функция, позволяющая добавить телефон для существующего клиента
4 - Функция, позволяющая изменить данные о клиенте
5 - Функция, позволяющая удалить телефон для существующего клиента
6 - Функция, позволяющая удалить существующего клиента
7 - Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)""")
    menu_number = input()
    if menu_number == '1':
        sql_func.create_db(conn)
    if menu_number == '2':
        os.system('clear')
        print("Введите фамилию:")
        first_name = input()
        print("Введите имя:")
        name = input()
        print("Введите почту:")
        email = input()
        user_id = sql_func.add_client(conn, name, first_name, email)
        print("Хотите добавить номер телефона? Y/N")
        phone_menu = input()
        if phone_menu == "Y":
            print("Введите номер телефона:")
            phone_number = input()
            sql_func.add_phone(conn, user_id, phone_number)
    if menu_number == '3':
        os.system('clear')
        print("Введите id пользователя:")
        user_id = input()
        print("Введите номер телефона:")
        phone_number = input()
        sql_func.add_phone(conn, user_id, phone_number)
    if menu_number == '4':
        os.system('clear')
        print("Введите id пользователя:")
        user_id = input()
        print("Введите новую фамилию:")
        first_name = input()
        print("Введите новое имя:")
        name = input()
        print("Введите новую почту:")
        email = input()
        print("Введите новый номер:")
        phone_number = input()
        sql_func.change_client(conn, user_id, first_name, name, email, phone_number)
    if menu_number == '5':
        os.system('clear')
        print("Введите id пользователя:")
        user_id = input()
        print("Введите номер телефона:")
        phone_number = input()
        sql_func.delete_phone(conn,user_id,phone_number)
    if menu_number == '6':
        os.system('clear')
        print("Введите id пользователя:")
        user_id = input()
        sql_func.delete_client(conn, user_id)
    if menu_number == '7':
        sql_func.find_client(conn)
conn.close()


