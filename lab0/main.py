import random as r

def del_marked_elem(spisok):
    index = 0
    while index < len(spisok):
        if spisok[index] == "del":
            spisok.pop(index)
            index = 0
        index = index + 1
    print("Выходной список: ", spisok)
def main():
    version = int(input("1. Ручной ввод;\n 2. Случайная генерация;\nВведите способ получения списка: "))
    match version:
        case 1:
            def get_korrect_spisok():
                while True:
                    try:
                        a = list(map(int, input("Введите значения списка: ").split()))
                        return a
                    except ValueError:
                        print('Введены некорректные данные. повторите ввод')

            spisok = get_korrect_spisok()
            print("Полученный список: ", spisok)
            maxNum = max(spisok)
            minNum = min(spisok)
            n1 = spisok.index(maxNum)
            n2 = spisok.index(minNum)

            if spisok.index(maxNum) + 1 == spisok.index(minNum):
                print("Минимальный элемент стоит сразу после максимального, удалять нечего;\nВыходной список: ", spisok)
                exit(0)

            if n2 + 1 == n1:
                print("Максимальный элемент стоит сразу после максимального, удалять нечего;\nВыходной список: ", spisok)
                exit(0)

            if n1 < n2:
                index = n1 + 1
                if index % 2 == 0:
                    for index in range(n1 + 1, n2):
                        if index % 2 == 0:
                            spisok[index] = 'del'
                if index % 2 != 0:
                    for index in range(n1 + 1, n2 + 1):
                        if index % 2 == 0:
                            spisok[index - 1] = "del"
                print("Список с отмеченными элементами, подлежащими удалению: ", spisok)
                del_marked_elem(spisok)

            if n2 < n1:
                index = n2 + 1
                if index % 2 == 0:
                    for index in range(n2 + 1, n1):
                        if index % 2 == 0:
                            spisok[index] = 'del'
                if index % 2 != 0:
                    for index in range(n2 + 1, n1 + 1):
                        if index % 2 == 0:
                            spisok[index - 1] = "del"
                print("Список с отмеченными элементами, подлежащими удалению: ", spisok)
                del_marked_elem(spisok)
        case 2:
            n = int(input("Введите размер списка: "))
            spisok = [r.randint(0, 10) for x in range(0, n)]
            print("Полученный список: ", spisok)
            maxNum = max(spisok)
            minNum = min(spisok)
            n1 = spisok.index(maxNum)
            n2 = spisok.index(minNum)

            if spisok.index(maxNum) + 1 == spisok.index(minNum):
                print("Минимальный элемент стоит сразу после максимального, удалять нечего;\nВыходной список: ", spisok)
                exit(0)

            if n2 + 1 == n1:
                print("Максимальный элемент стоит сразу после минимального, удалять нечего;\nВыходной список: ", spisok)
                exit(0)

            if n1 < n2:
                index = n1 + 1
                if index % 2 == 0:
                    for index in range(n1 + 1, n2):
                        if index % 2 == 0:
                            spisok[index] = 'del'
                if index % 2 != 0:
                    for index in range(n1 + 1, n2 + 1):
                        if index % 2 == 0:
                            spisok[index - 1] = "del"
                print("Список с отмеченными элементами, подлежащими удалению: ", spisok)
                del_marked_elem(spisok)

            if n2 < n1:
                index = n2 + 1
                if index % 2 == 0:
                    for index in range(n2 + 1, n1):
                        if index % 2 == 0:
                            spisok[index] = 'del'
                if index % 2 != 0:
                    for index in range(n2 + 1, n1 + 1):
                        if index % 2 == 0:
                            spisok[index - 1] = "del"
                print("Список с отмеченными элементами, подлежащими удалению: ", spisok)
                del_marked_elem(spisok)
if __name__ == "__main__":
    main()