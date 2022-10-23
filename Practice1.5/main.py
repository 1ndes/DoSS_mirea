import zipfile
import os

def createFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Введите название ZIP файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    zip_archive = zipfile.ZipFile(file + '.zip', mode='w')
    zip_archive.close()

def infoZIP():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Введите название ZIP файла >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    zip_archive = zipfile.ZipFile(file + '.zip', "w")
    filen = (input ('Введите название файла с расширением, который необходимо архивировать >> '))
    if os.path.exists(filen):
        zip_archive.write(filen)
        zip_archive.close
    else:
        print('Файл не найден')
        zip_archive.close()

def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Введите название ZIP файла >> '))
    zip_archive = zipfile.ZipFile(file + '.zip', 'r')
    zip_archive.extractall('.')
    print('Файл ZIP прочитан')
    for file_info in zip_archive.infolist(): 
        print(file_info.filename, file_info.date_time, file_info.file_size)
    zip_archive.close()

def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    zip = (input ('Введите название ZIP файла >> '))
    filen = (input ('Введите название файла с расширением, который необходимо удалить >> '))
    if os.path.exists(zip + ".zip"):
        os.remove(zip + ".zip")
    else:
        print('Файл не найден')
    if os.path.exists(filen):
        os.remove(filen)
    else:
        print('Файл не найден')

actions = {
    1: createFile,
    2: infoZIP,
    3: readData,
    4: deleteFile
}
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Создать архив')
    print('2. Добавить файл в архив')
    print('3. Разархивировать ZIP и показать информацию')
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