from dbmanager import DatabaseManager

if __name__ == "__main__":
    db = DatabaseManager("example.db")

    # Создание таблиц
    db.create_tables()

    # # Добавление пользователей
    # nike_id = db.add_user("Nike", "Nike@example.com")
    # mike_id = db.add_user("Mike", "mike@example.com")

    # # Добавление заказов
    # db.add_order(alice_id, "Laptop", 1)
    # db.add_order(alice_id, "Mouse", 2)
    # db.add_order(bob_id, "Keyboard", 1)
    # db.add_order(nike_id, "Headphones", 3)
    # db.add_order(mike_id, "Mouse", 1)

    # получение и вывод данных о пользователях
    result = db.get_user_data(2)

    # Проверка, что данные были найдены
    if result:
        print(f"[Name: {result[0]}, Email: {result[1]}]")
    else:
        print("Пользователь не найден")

    # Добавление адреса
    # db.add_address(1, "123 Main St", "New York", "NY", "10001")
    # db.add_address(2, "456 Elm St", "Los Angeles", "CA", "90001")
    # db.add_address(3, "789 Oak St", "San Francisco", "CA", "94101")

    # Получение и вывод данных о заказах пользователей
    results = db.get_user_orders()
    for row in results:
        print(f"User: {row[0]} ({row[1]}), Product: {row[2]}, Quantity: {row[3]}")

    # Закрытие соединения с базой данных
    db.close()
