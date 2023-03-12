import csv
from tabulate import tabulate

# Функция открытия меню
def open_main_menu():
  print("\n" + "--"*55 + "\n" +
        "\033[32mПриложение заметки\033[0m\n" + "--"*55)
  print("\033[33mОткрыть меню?\033[0m\n")
  menu_list = [
    "1. Да",
    "2. Нет"
    ]
  for item in menu_list:
    print(item)

# Функция выбора пользователя открытия основного меню
# и проверка на правильность ввода
def get_user_choice():
    while True:
        try:
            choice = int(
                input("--"*55 + "\n" + "\033[36mСделайте свой выбор: \033[0m"))
            if choice > 0 and choice < 3:
                return choice
            else:
                print(
                    "\n\033[31mНеверный ввод. Пожалуйста, введите число от 1 до 2!!!\033[0m")
        except ValueError:
            print(
                "\n\033[31mНеверный ввод. Пожалуйста, введите число от 1 до 2!!!\033[0m")

# Функция открытия основного меню пользователя
def display_notes_menu():
  print("--"*55 + "\n" + "\033[33mОсновное меню пользователя:\n\033[0m")
  menu_list = [
    "1. Посмотреть все заметки",
    "2. Добавить заметку",
    "3. Редактировать заметку",
    "4. Удалить заметку",
    "5. Сделать выборку заметок по дате добавления",
    "6. Выход"
    ]
  for item in menu_list:
    print(item)

# Функция выбора пункта основного меню для выполнения действия
# и проверка на правильность ввода
def user_choice_menu_item():
    while True:
        try:
            choice = int(
                input("--"*55 + "\n" + "\033[36mВыберите действие: \033[0m"))
            if choice > 0 and choice < 7:
                return choice
            else:
                print(
                    "\n\033[31mНеверный ввод. Пожалуйста, введите число от 1 до 6!!!\033[0m")
        except ValueError:
            print(
                "\n\033[31mНеверный ввод. Пожалуйста, введите число от 1 до 6!!!\033[0m")

# Функция вывода заголовка перед открывшемся списком всех заявок
def notes_list():
  print("--"*55 + "\n" + "\033[33mСписок всех заметок: \n\033[0m")

#Функция добавления заметки
def adding_notes():
    print("--"*55 + "\n" + "\033[33mДобавить заметку: \033[0m")
    header = input("\n\033[36mВведите заголовок заметки: \033[0m")
    description = input("\n\033[36mВведите описание заметки: \033[0m")
    print("--"*55 + "\n" + "\033[35mЗаметка добавлена в приложение!!! \033[0m")
    return header, description

#Функция редактирования заметки 
def edit_note(file):
    print("--"*55 + "\n" + "\033[33mРедактировать заметку: \033[0m")
    try:
        id = int(input("\n\033[36mВведите ID заметки, которую вы хотите изменить: \033[0m"))
    except ValueError:
        print("--"*55 + "\n" + "\033[31mНеверный ввод. Пожалуйста, введите число!!!\033[0m")
        return None
    
    notes = []
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        notes.append(row)
      
    title = None
    body = None
    if id not in [int(note[0]) for note in notes]:
        print("--"*55 + "\n" + "\033[31mНеверный ID. Такая заметка отсутствует в списке!!!\033[0m")
        return None
    else:
        notes = [note for note in notes if int(note[0]) != id]
        title = input("\n\033[36mВведите новый заголовок заметки (можно оставить незаполненным): \033[0m") or None
        body = input("\033[36mВведите новое описание заметки (можно оставить незаполненным): \033[0m") or None
        print("--"*55 + "\n" + "\033[35mЗаметка отредактирована!!! \033[0m")
    return id, title, body

#Функция удаления заметки
def ask_delete_note(file):
    print("--"*55 + "\n" + "\033[33mУдалить заметку: \033[0m")
    try:
        id_to_delete = int(input("\n\033[36mВведите ID заметки, которую вы хотите удалить: \033[0m"))
    except ValueError:
        print("--"*55 + "\n" + "\033[31mНеверный ввод. Пожалуйста, введите число!!!\033[0m")
        return None

    notes = []
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        notes.append(row)

    if id_to_delete not in [int(note[0]) for note in notes]:
        print("--"*55 + "\n" + "\033[31mНеверный ID. Такая заметка отсутствует в списке!!!\033[0m")
    else:
        notes = [note for note in notes if int(note[0]) != id_to_delete]
        print("--"*55 + "\n" + "\033[35mЗаметка успешно удалена!!!\033[0m")
    return id_to_delete
  
#Функция ввода даты для поиска заметок
def addition_date_selection():
    print("--"*55 + "\n" + "\033[33mВыборка заметок по дате добавления: \033[0m")
    date_selection = input("\n\033[36mВведите дату для поиска, формат ввода (дд.мм.гггг): \033[0m")
    return date_selection

#Функция вывода результата выборки заметок по дате
def display_notes(result):
  print("--"*55 + "\n" + "\033[35mРезультат поиска:\033[0m")
  print(tabulate(result, headers=['\033[91mID\033[0m', '\033[91mЗаголовок\033[0m', '\033[91mОписание заметки\033[0m',
                                  '\033[91mДата/время создания\033[0m', 
                                  '\033[91mДата/время изменения\033[0m'], tablefmt="fancy_grid", stralign="center"))

# Функция вывода сообщение при завершении работы
def application_closing():
    print("--"*55 + "\n" + "\033[35mВы завершили работу в приложении!!!\033[0m")
