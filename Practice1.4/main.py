import os
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET


def createFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Введите название файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open (file + ".xml", "w") as f:
        mainElement = (input('Название основного элемента >> '))
        mainET = ET.Element(mainElement)
        loop = int((input('Сколько саб-элементов в основном? >>')))
        i=0
        for i in range(i,loop):
            sEL = (input('Введите название саб-элемента >>'))
            sELval = (input('Введите значение саб-элемента >>'))
            ET.SubElement(mainET,sEL).text = sELval
        ET.dump(mainET)
        tree = ET.ElementTree(mainET)
        tree.write(file + ".xml",encoding="UTF-8")
        f.close()
    if os.path.exists(file + ".xml"):
        print('Файл ' + file + '.xml' +' создан')
    else:
        print('Файл не найден')


def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Введите название XML файла >> '))
    if os.path.exists(file + ".xml"):
        with open (file + ".xml", "r") as f:
            tree=ET.parse(file + ".xml")
            mainET = tree.getroot()
            print('<' + mainET.tag + '>') 
            for child in mainET:
                print(' <'+child.tag + '>')
                print('  <'+child.text + '>')
            f.close()
    else:
        print('Файл не найден')

def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Введите название XML файла >> '))
    if os.path.exists(file + ".xml"):
        os.remove(file + ".xml")
    else:
        print('Файл не найден')

actions = {
    1: createFile,
    2: readData,
    3: deleteFile
}
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Создать файл и вписать данные')
    print('2. Прочитать данные с файла')
    print('3. Удалить файл')
    print('4. Выход')

    while True:
        action = int(input('>> '))
        if action == 4:
            exit(0)
        else:
            if action in actions:
                actions[action]()

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    main()