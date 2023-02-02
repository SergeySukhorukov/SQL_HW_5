import os

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS client (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
            );
        """)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS phone_number (
                id SERIAL PRIMARY KEY,
                number TEXT NOT NULL UNIQUE,
                client_id INTEGER NOT NULL REFERENCES client(id)
                );
            """)
        conn.commit()
    pass

def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute(f"""
                    INSERT INTO public.client
                    (name, surname, email)
                    VALUES('{first_name}', '{last_name}', '{email}') RETURNING id;
                    """)
        for id in cur.fetchone():
            user_id = id
    conn.commit()
    return user_id
    pass

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute(f"""
                    INSERT INTO public.phone_number
                    ("number", client_id)
                    VALUES({phone}, {client_id}) ;
                 """)
    conn.commit()
    pass

def change_client(conn, client_id, first_name, last_name, email, phone):
    with conn.cursor() as cur:
        cur.execute(f"""
                    UPDATE public.client
                    SET "name"='{last_name}', "surname"='{first_name}', "email"='{email}'
                    WHERE id={client_id};
                    UPDATE public.phone_number
                    SET "number"='{phone}'
                    WHERE client_id={client_id};
""")
    conn.commit()
    pass

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute(f"""
        DELETE FROM public.phone_number
        WHERE client_id='{client_id}' AND number='{phone}';
    """)
    conn.commit()
    pass

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute(f"""
        DELETE FROM public.phone_number
        WHERE client_id='{client_id}';
        DELETE FROM public.client
        WHERE id='{client_id}';
    """
    )
    conn.commit()
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    os.system('clear')
    print("""По какому параметру выполнять поиск?
    1-Имя
    2-Фамилия
    3-Почта
    4-Телефон""")
    search_menu=input()
    if search_menu == "1":
        print("Введите имя")
        first_name=input()
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT client.id, client.name, client.surname, client.email, phone_number.number
            FROM public.client
            LEFT JOIN phone_number ON phone_number.client_id = client.id
            WHERE client.name ='{first_name}';""")
            print(cur.fetchall())
        conn.commit()
    if search_menu == "2":
        print("Введите фамилию")
        last_name=input()
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT client.id, client.name, client.surname, client.email, phone_number.number
            FROM public.client
            LEFT JOIN phone_number ON phone_number.client_id = client.id
            WHERE client.surname ='{last_name}';""")
            print(cur.fetchall())
        conn.commit()
    if search_menu == "3":
        print("Введите почту")
        email=input()
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT client.id, client.name, client.surname, client.email, phone_number.number
            FROM public.client
            LEFT JOIN phone_number ON phone_number.client_id = client.id
            WHERE client.email ='{email}';""")
            print(cur.fetchall())
        conn.commit()
    if search_menu == "4":
        print("Введите телефон")
        phone=input()
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT client.id, client.name, client.surname, client.email, phone_number.number
            FROM public.client
            LEFT JOIN phone_number ON phone_number.client_id = client.id
            WHERE phone_number.number ='{phone}';""")
            print(cur.fetchall())
        conn.commit()

    pass

