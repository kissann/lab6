#Задача 1
#Створіть словник school, і наповніть даними, які б відображали кількість учнів в різних класах (1а, 1б, 2б, 6а, 7в).
# Внесіть зміни в словник відповідно до наступного: а) в одному з класів змінилася кількість учнів,
# б) в школі з'явився новий клас,
# с) в школі був розформований (вилучено) інший клас.
# Обчисліть загальну кількість учнів у школі.
# Передбачте створення консольного інтерфейсу для виконання зазначених дій та виходу із програми.
school={'1a':20,'1b':30,'1c':10,'2b':30}
flag=True

while flag:
    count = 0
    act=input("Введите действие:\na- додати учнів в клас\nb - создать новый класс\nс - в школі був розформований (вилучено) інший клас\nДля "
              "выхода нвведите ^")
    if act=='^':
        flag=False
        break
    elif act=='a':
        klass=input("Введите класс в который хотите добавить учеников (пример 1a):")
        for i in school.keys():
            if i==klass:
                kol=input("Введите количество прибывших учеников:")
                sum=school.get(i)+int(kol)
                school[i]=sum
            count=int(count)+school[i]
    elif act=='b':
        klass = input("Введите новый класс:")
        school[klass] = 0
        kol = input("Введите количество учеников:")
        sum=school[klass]=kol

    elif act=='c':
        klass = input("Введите  класс который был расформирован:")
        del school[klass]

    for i in school.keys():
        count = int(count) + int(school[i])

    print(school)
    print("Количество учеников : ",count)