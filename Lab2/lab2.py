# Массивы
# Минимальное
def minimum(a):
    min = a[0]
    for i, el in enumerate(a):  # Берем каждый элемент массива
        if el < min:            # Если он меньше минимального, то
            min = el            # Присваеваем его значение минимальному
    return (min)


# Среднее арифметическое
def average(a):
    sum = 0
    for i, el in enumerate(a):
        sum = sum + el         # Суммируем все элементы массива
    return (sum / (i + 1))     # Возвращаем суммы деленую на количество


a = [3, 1, 2]
print(minimum(a))
print(average(a))


# Строки

def reverse(str):
    j = 0
    str2 = ''
    for i in range(len(str)):
        b = len(str) - j - 1   # Перебираем строку с конца
        str2 = str2 + str[b]   # Добавляем символ к новой строке
        j = j + 1
    print(str2)


reverse("Hello, world!")


# Словари

def childrens(emps):
    for i, el in enumerate(emps):         # Обходим массив родителей
        emp = el['children']
        for i, child in enumerate(emp):   # Обходим массив детей
            if child['age'] > 18:         # Если возраст ребенка больше 18
                print(el['name'])         # Выводим имя родетеля


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan, darja]
childrens(emps)
