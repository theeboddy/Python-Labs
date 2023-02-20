import os
from pathlib import Path
import csv

def countFiles():
    fileName = input("Введите путь к папке: ")
    file = Path(fileName)
    files = os.listdir(file)
    print(f"В данной папке содержатся следующие объекты: {files}\nИх количество: {len(files)}")

def get_BD_to_Dict(moveHistory):
    print("movement number;date and time;workplace sign;room number")
    with open("BD.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(*row)
            moveHistory[row[0]] = row[1:]

def sort_movement_number(moveHistory):
    print("\nОтсортируем словарь по номеру комнаты работников: ")
    # sortMoveHistory = dict(sorted(moveHistory.items(), key=lambda item: item[2]))
    for elem in sorted(moveHistory.items(), key = lambda para: int(para[1][2])):
        print(elem[0], *elem[1])

def sort_movement_str(moveHistory):
    print("\nОтсортируем словарь по признаку рабочего стола работников: ")
    # sortMoveHistory = dict(sorted(moveHistory.items(), key=lambda item: item[2]))
    for elem in sorted(moveHistory.items(), key = lambda para: para[1][1]):
        print(elem[0], *elem[1])
    print("")

def output_by_criterion(moveHistory):
    criterion = input("Введите признак рабочего стола: \n")
    print(f'\nСтроки, в которых признак рабочего стола "{criterion}": ')
    for elem in moveHistory:
        if moveHistory[elem][1] == criterion:
            print(elem, *moveHistory[elem])

def write_to_csv(moveHistory):
    newKey = input("Введите номер перемещения (ключ): ")
    newDate = input("Введите дату и время через точку с запятой: ")
    newWorkplaceSign = input("Введите признак рабочего стола: ")
    newRoomNumber = input("Введите номер комнаты: ")
    moveHistory[newKey] = [newDate, newWorkplaceSign, newRoomNumber]
    with open('BD.csv', 'w', encoding='utf-8') as f:
        for elem in moveHistory:
            f.write(elem + ',' + moveHistory[elem][0] + ',' + moveHistory[elem][1] + ',' + moveHistory[elem][2] + '\n')


def main():
    countFiles()
    moveHistory = {}
    get_BD_to_Dict(moveHistory)
    sort_movement_number(moveHistory)
    sort_movement_str(moveHistory)
    output_by_criterion(moveHistory)
    write_to_csv(moveHistory)
if __name__ == "__main__":
    main()

