import os

file_path = "/"


def createFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Впишите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open(file + ".txt", "w") as f:
        f.close()
    if os.path.exists(file + ".txt"):
        print('Файл ' + file + '.txt' + ' был создан!')
    else:
        print('Файл не создан')


def writeDataToFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Впишите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    if os.path.exists(file + ".txt"):
        print('Хотите очистить файл? (y/n)')
        checkAns = (input(">> "))
        os.system('clear' if os.name == 'posix' else 'cls')
        if checkAns == 'y' or checkAns == 'Y':
            print("Файл очищен. Напишите строчку для записи в файл ")
            data = (input(">> "))
            os.system('clear' if os.name == 'posix' else 'cls')
            with open(file + ".txt", "w") as f:
                f.write(data + '\n')
                f.close()
            print('Строка добавлена')
        else:
            print("Напишите строчку для записи в файл ")
            data = (input(">> "))
            os.system('clear' if os.name == 'posix' else 'cls')
            with open(file + ".txt", "a+") as f:
                f.write(data + '\n')
                f.close()
            print('Строка добавлена')
    else:
        print('Файл не создан')


def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Впишите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    if os.path.exists(file + ".txt"):
        with open(file + ".txt", "r") as f:
            print("Данные файла " + file + ".txt " + ":" + "\n")
            print(f.read())
            f.close()
    else:
        print('Файл не создан')


def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Впишите название файла >> '))
    if os.path.exists(file + ".txt"):
        os.remove(file + ".txt")
    else:
        print('Файл не создан')


actions = {
    1: createFile,
    2: writeDataToFile,
    3: readData,
    4: deleteFile
}


def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Создать файл')
    print('2. Записать данные в файл')
    print('3. Прочитать данные из файла')
    print('4. Удалить файл')
    print('5. Выход')

    while True:
        action = int(input('>> '))
        if action == 5:
            exit(0)
        else:
            if action in actions:
                actions[action]()


if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    main()