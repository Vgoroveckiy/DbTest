import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Создание таблицы users
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """
        )

        # Создание таблицы orders
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )
            """
        )

        # Создание таблицы addresses
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                street TEXT NOT NULL,
                city TEXT NOT NULL,
                country TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )
            """
        )

        self.conn.commit()

    # добавление пользователя
    def add_user(self, name, email):
        self.cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (?, ?)
            """,
            (name, email),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    # добавление заказа
    def add_order(self, user_id, product_name, quantity):
        self.cursor.execute(
            """
            INSERT INTO orders (user_id, product_name, quantity)
            VALUES (?, ?, ?)
            """,
            (user_id, product_name, quantity),
        )
        self.conn.commit()

    # получение данных о заказах
    def get_user_orders(self):
        self.cursor.execute(
            """
            SELECT users.name, users.email, orders.product_name, orders.quantity
            FROM orders
            JOIN users ON orders.user_id = users.id
            """
        )
        return self.cursor.fetchall()

    # добавление адреса
    def add_address(self, user_id, street, city, country):
        self.cursor.execute(
            """
            INSERT INTO addresses (user_id, street, city, country)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, street, city, country),
        )
        self.conn.commit()

    # получение данных пользователя
    def get_user_data(self, user_id):
        self.cursor.execute(
            """
            SELECT name, email
            FROM users
            WHERE id = ?
            """,
            (user_id,),
        )
        return self.cursor.fetchone()

    # закрытие соединения
    def close(self):
        self.conn.close()
