import win32com.client


def main():
    print("---------------------------------------")

    strComputer = "."
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer, "root\cimv2")
    colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk")

    for objItem in colItems:
        print("Наименование диска: ", objItem.Name)
        print("Название диска: ", objItem.VolumeName)
        gigMemory = int(int(objItem.Size) / 1024 / 1024 / 1024)
        print("Размер: ", objItem.Size, "байт = ", gigMemory, "гигабайт")
        print("Файловая система: ", objItem.FileSystem)
        print("---------------------------------------")


if __name__ == '__main__':
    main()
