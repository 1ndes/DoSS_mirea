import os
import json

file_path = "/"


def createObject():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Напишите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open(file + '.json', 'w') as f:
        if os.path.exists(file + ".json"):
            Dictionary = {}
            os.system('clear' if os.name == 'posix' else 'cls')
            key = input('Введите ключ >>')
            value = input('Введите значение ключа >>')
            Dictionary[key] = value
            key = input('Введите второй ключ >>')
            value = input('Введите значение ключа >>')
            Dictionary[key] = value
            key = input('Введите последний ключ >>')
            value = input('Введите значение ключи >>')
            Dictionary[key] = value
            json.dump(Dictionary, f, indent=4)
            f.close()
            print('Файл с расширением JSON был создан')
        else:
            print('Файл не найден')


def writeDataToFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Напишите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open(file + '.json', 'w') as f:
        if os.path.exists(file + ".json"):
            Dictionary = {}
            os.system('clear' if os.name == 'posix' else 'cls')
            key = input('Введите ключ >>')
            value = input('Введите значение ключа >>')
            Dictionary[key] = value
            key = input('Введите второй ключ >>')
            value = input('Введите значение ключа >>')
            Dictionary[key] = value
            key = input('Введите последний ключ >>')
            value = input('Введите значение ключа >>')
            Dictionary[key] = value
            json.dump(Dictionary, f, indent=4)
            f.close()
            print('Файл с расширением JSON был обновлен')
        else:
            print('Файл не найден')


def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Напишите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    if os.path.exists(file + ".json"):
        with open(file + ".json", "r") as f:
            print("Данные файла " + file + ".json " + ":" + "\n")
            data = json.load(f)
            print(data)
            f.close()
    else:
        print('Файл не найден')


def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input('Напишите название файла >> '))
    if os.path.exists(file + ".json"):
        os.remove(file + ".json")
    else:
        print('Файл не найден')


actions = {
    1: createObject,
    2: writeDataToFile,
    3: readData,
    4: deleteFile
}


def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Создать JSON файл')
    print('2. Добавить объект в существующий файл')
    print('3. Прочитать данные из JSON')
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