import json
import os

# Функция для загрузки данных из файла в телефонную книгу
def load_phone_book(file_name):
    phone_book = {}
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            phone_book = json.load(file)
    return phone_book

# Функция для сохранения данных из телефонной книги в файл
def save_phone_book(phone_book, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json.dumps(phone_book, ensure_ascii=False))

# Функция для просмотра всех контактов в телефонной книге
def view_contacts(phone_book):
    print("Телефонная книга:")
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("Телефонная книга пуста.")

# Функция для добавления нового контакта
def add_contact(phone_book, name, number):
    phone_book[name] = number
    print(f"Контакт {name} добавлен.")

# Функция для удаления контакта
def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} удален.")
    else:
        print(f"Контакт {name} не найден.")

# Функция для поиска контакта
def find_contact(phone_book, name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"Контакт {name} не найден.")

# Функция для изменения контакта
def change_contact(phone_book, name, number):
    phone_book[name] = number
    print(f"Контакт {name} изменен.")

file_name = "contacts.json"
contacts = load_phone_book(file_name)

while True:
    print("\nМеню:")
    print("1. Просмотреть контакты")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Найти контакт")
    print("5. Изменить контакт")
    print("6. Сохранить контакты в файл")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        view_contacts(contacts)
    elif choice == '2':
        name = input("Введите имя: ")
        number = input("Введите номер телефона: ")
        add_contact(contacts, name, number)
    elif choice == '3':
        name = input("Введите имя контакта, который нужно удалить: ")
        delete_contact(contacts, name)
    elif choice == '4':
        name = input("Введите имя контакта, который нужно найти: ")
        find_contact(contacts, name)
    elif choice == '5':
        name = input("Введите имя: ")
        number = input("Введите новый номер телефона: ")
        change_contact(contacts, name, number)
    elif choice == '6':
        save_phone_book(contacts, file_name)
        print("Контакты сохранены в файл.")
    elif choice == '7':
        break
    else:
        print("Не правильный выбор! Выберите вариант из пречня.")
