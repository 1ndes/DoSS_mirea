import stat
import string
import os.path
import itertools
import hashlib
import time
from threading import Thread
# use Multiprocessing w/o Thread

save_path = 'C:/Sereja/BPO/Practice2/test'
count = 0
password1 = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
password2 = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
password3 = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"


def createFileWithPasswords():
    os.chmod(save_path, stat.S_IRWXU)
    completeName = os.path.join(save_path, "test.txt")
    if os.path.exists(completeName) == True:
        print("Файл с таким названием уже существует")
    else:
        file = open(completeName, "w")
        for i in itertools.product(string.ascii_lowercase, repeat=5):
            file.write(''.join(i) + '\n')
        file.close()

def FileWithHashPasswords():
    completeName = os.path.join(save_path, "passwords.txt")
    file = open(completeName, "w")
    file.write(password1+'\n'+password2 + '\n' + password3)

def convertToHash(text):
    encrypted = hashlib.sha256(text.encode()).hexdigest()
    return encrypted

def compare():
    start_time = time.time()
    global count
    completeName = os.path.join(save_path, "test.txt")
    file = open(completeName, "r")
    for i in range(5**26):
        line = file.readline()[:-1]
        convertedLine = convertToHash(line)
        if convertedLine == password1 or convertedLine == password2 or convertedLine == password3:
            answer = line
            print("Пароль = " + answer + ", SHA-256: " + convertedLine + ", Затраченное время = %s секунд" % (time.time() - start_time))
            count += 1
        if count == 3:
            break
    file.close()
    pass

def compareWithThread(i, lines, n):
    start_time = time.time()
    global count
    completeName = os.path.join(save_path, "test.txt")
    if os.path.exists(completeName):
        print("n="+str(i))
        for line in range(int((len(lines)/n)*i), int((len(lines)/n)*(i+1))):
            convertedLine = convertToHash(lines[line][:-1])
            if convertedLine == password1 or convertedLine == password2 or convertedLine == password3:
                answer = lines[line][:-1]
                print("Пароль = " + answer + ", SHA-256: " + convertedLine + ", Затраченное время = %s секунд" % (time.time() - start_time))
                count += 1
            if count == 3:
                break
    else:
        print("Файла с таким именем не существует")
    pass

def Threads(n):
    completeName = os.path.join(save_path, "test.txt")
    file = open(completeName, "r")
    lines = file.readlines()
    file.close()
    for i in range(n):
        thread = Thread(target=compareWithThread, args=(i, lines, n))
        thread.start()

work = True
createFileWithPasswords()
while work:
    print("Выбор работы программы:")
    print("1 | Однопоточный")
    print("2 | Многопоточный")
    check = input("Введите значение: ")
    if check == "1":
        compare()
        work = False
    elif check == "2":
        print("Количество потоков")
        thr = input("Введите значение: ")
        if thr.isnumeric():
            Threads(int(thr))
            work = False
        else:
            print("Внимание - нецелочисленное значение: ")
    else:
        print("Внимание - неверное значение: ")
