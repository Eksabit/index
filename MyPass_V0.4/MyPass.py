from cryptography.fernet import Fernet
from colorama import Fore, Back, Style, init, just_fix_windows_console
from tqdm import trange, tqdm
from time import sleep
import random
import ctypes
import os
just_fix_windows_console()
ctypes.windll.kernel32.SetConsoleTitleA(b"MyPass V0.4")
def progress_bar():
    with tqdm(total=100) as pbar:
        for i in range(100):
            sleep(0.1)
            pbar.update(1)
def logo():
    print(Fore.GREEN + '''
   ──╔╗───╔═╗───────────╔╗────
    ╔╝║╔═╗║╬║╔══╗╔═╗╔═╗╔╝║
    ║╬║║╬║╠╗║║║║║║╬║║╬║║╬║
    ╚═╝╚═╝╚═╝╚╩╩╝╚═╝╚═╝╚═╝ ☭
    MyPass V0.4
   ───────────────────────────''')
logo()
print('Загрузка...')
progress_bar()
print(Fore.RED + '''
1 - Создать или загрузить приватный ключ
2 - Создать список паролей (file_open.txt)
3 - Зашифровать (file_closed.txt)
4 - Расшифровать (file_open.txt)
5 - Сгенерировать надежные пароли
6 - Показать приватный ключ
7 - Выход из программы
Для вывода справки наберите "help"
''')
def check_filePuzzle(): #Функция проверки ключа
    key = Fernet.generate_key() #Создание экземпляра класса, использующего ключ
    if os.path.isfile("Puzzle.key"): #Проверяем наличие ключа
        with open('Puzzle.key', 'rb') as f: #Если ключа нету то создаем его
            key = f.read()
            print(Fore.YELLOW + 'Ключ успешно загружен')
    else:
        with open('Puzzle.key', 'wb') as f:
            f.write(key)
            print(Fore.YELLOW + 'Был создан новый ключ: ', key)
def save_private_password(): #Функция записи информации в файл
    if os.path.exists('file_open.txt'):
        print(Fore.YELLOW + 'У Вас уже есть файл с паролями! (file_open.txt)')
        menu_MyPass()
    elif os.path.exists('file_closed.txt'):
        print(Fore.YELLOW + 'У Вас уже есть файл с паролями! (file_closed.txt)')
        menu_MyPass()
    else:
        print(Fore.YELLOW + 'Создан новый файл!')
        with open('file_open.txt', 'w', encoding='utf-8') as B:
            B.write('Мои пароли: ')
            B.close()
            menu_MyPass()

def open_private_key(): #Показать приватный ключ
    try:
        f = open('Puzzle.key', 'r', encoding='utf-8')
        print(f.read())
    except:
        print(Fore.YELLOW + 'Файл отсутствует!')

def Encrypt(): # Шифрование файла
    if os.path.exists('file_open.txt') and os.path.exists('Puzzle.key'):
        with open('Puzzle.key', 'rb') as f:
            key = f.read()
            fernet = Fernet(key)
        with open('file_open.txt', 'rb') as f:
            plaintext = f.read()
            encrypted = fernet.encrypt(plaintext)
        with open('file_open.txt', 'wb') as f:
            f.write(encrypted)
            f.close()
            os.rename('file_open.txt', 'file_closed.txt')
            print(Fore.YELLOW + 'Файл зашифрован!')
            menu_MyPass()
    else:
        print(Fore.YELLOW + 'Отсутствует файл ключа или файл с паролями!')
        menu_MyPass()

def Decrypt():
    if os.path.isfile('file_closed.txt') and os.path.exists('Puzzle.key'):
        with open('Puzzle.key', 'rb') as f:
            key = f.read()
            fernet = Fernet(key)
        with open('file_closed.txt', 'rb') as f:
            encrypted = f.read()
            decrypted = fernet.decrypt(encrypted)
        with open('file_closed.txt', 'wb') as f:
            f.write(decrypted)
            f.close()
            os.rename('file_closed.txt', 'file_open.txt')
            print(Fore.YELLOW + 'Файл расшифрован!')
            menu_MyPass()
    else:
        print(Fore.YELLOW + 'Отсутствует файл ключа или файл с паролями!')
        menu_MyPass()

def exit_MyPass(): #Функция выхода из программы
    exit_edit = input(Fore.YELLOW + 'Выйти из программы? y/n: ')

    if exit_edit == 'y' and 'n':
        print(Fore.YELLOW + 'Выгружаюсь...')
        raise SystemExit
    else:
        print(Fore.YELLOW + 'Команда не распознана...')
        menu_MyPass()

def PassGen():
    ver = "ver: 0.1 \n"
    a = ["сложный", "пароль", ":",
        "Генератор сложных паролей "]
    chars = '+-/*$&#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    print(a[3], ver)
    num = int(input(Fore.YELLOW + "количество паролей: "))
    hard = int(input(Fore.YELLOW + "сложность: "))

    password_list = []

    for b in range(num):
        c = ''
        for i in range(hard):
            c += random.choice(chars)
        print(b, a[0], a[1], a[2], c)
        ListPass = ''.join(c)
        password_list.append(ListPass)

    MyFile = open('Pass.txt', 'w')

    for element in password_list:
        MyFile.write(element)
        MyFile.write('\n')
    MyFile.close()

    print(Fore.YELLOW + "Пароли в колличестве ", b, "штук сгенерированны \n")
    input(Fore.YELLOW + "Нажмите любую клавишу для выхода...")
    menu_MyPass()

def menu_MyPass(): #Функция консольного меню
    menu = input(Fore.RED + 'Ввод: ')

    if menu == '1':
        check_filePuzzle()
        menu_MyPass()
    if menu == '2':
        save_private_password()
        menu_MyPass()
    if menu == '3':
        Encrypt()
        menu_MyPass()
    if menu == '4':
        Decrypt()
        menu_MyPass()
    if menu == '5':
        print(Fore.YELLOW + 'Сгенерировать пароли: ')
        PassGen()
        menu_MyPass()
    if menu == '6':
        print(Fore.YELLOW + 'Это ваш приватный ключ: ')
        open_private_key()
        menu_MyPass()
    if menu == 'help':
        help_cmd()
        menu_MyPass()
    if menu == '7':
        exit_MyPass()
    else:
        print(Fore.YELLOW + 'Такой команды тут нет')
        menu_MyPass()

def help_cmd():
    logo()
    print(Fore.YELLOW + '''
    Привет Дорогой друг!

    MyPass - это аналог программы KeePass созданный для личных нужд.
    Она умеет шифровать текстовой файл file.txt алгоритмом шифрования AES256

    [1 - Создать или загрузить приватный ключ] = Генерирует ключ для шифрования текстовых файлов, без него не чего не получится.
    [2 - Создать список паролей (file_open.txt)] = Создает простой текстовой файл file_open.txt и больше не чего.
    [3 - Зашифровать (file_closed.txt)] = Шифрует file_open.txt алгоритмом AES-128 и меняет имя файла на file_closed.txt (при условии что вы создали ключ).
    [4 - Расшифровать file_open.txt)] = Расшифровывает file_closed.txt и меняет имя файла на file_open.txt (при условии что вы создали ключ).
    [5 - Сгенерировать надежные пароли] = Генерирует дофига паролей в файлик Pass.txt.
    [6 - Показать приватный ключ] = Покажет приватный ключ что бы вы могли его скопировать и передать другу в Телегу.
    [7 - Выход из программы] = Выход из программы... да я знаю, можно просто закрыть консоль, но мне захотелось добавить такую прикольную фишку так шо идите нафиг... =)

    Вопрос: Как я могу использовать программу?
    Ответ: Очень просто. Кидаешь её на флешку, создаешь ключ для шифрования и генерируешь файлик с паролями (file_open.txt),
    записываешь в этот файлик свои логины и пароли, шифруешь его и оставляешь на компе.
    Когда нужно подглядеть забытый пароль то скидываешь file_closed.txt назад к себе на флешку, расшифровываешь и смотришь свои пароли.

    Вопрос: Чёт какие-то костыли?
    Ответ: Возможно. Но зато система надежна как автомат Калашникова. Чем проще, Тем надежнее.
    
    Совет: Запускайте прогу из отдельной папочки что бы не искать потом ключи и файлы, прога все сложит в одну папку.

    Отдельная благодарность: @FORTYSIXm за вчерашний "бета тест" Я учёл все твои пожелания братан! 

    Ссылки: 
    https://dogmood.ru 
    https://github.com/Eksabit
    ''')
    menu_MyPass()

menu_MyPass()