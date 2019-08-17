#Задача 3
#Необхідно реалізувати пошук даних за унікальним значенням телефонного номера
# у текстовому файлі (створити самостійно із розширенням txt).
f = open('phone.txt', 'r')
sp={}
k=0
for line in f:
    str=list(line.split(' '))
    phone=str[1]
    sp[phone] = 0

    del str[1]
    sp[phone] = str
    k=k+1
flag=True
while flag:
    ph=input("Введите номер телефона; Для выхода ^")
    answer={}
    answer1=''
    for i in sp.keys():
        if i==ph:
            answer=list(sp.get(i))
        elif ph=='^':
            flag=False
            break
        else:
            answer1="Нет такой записи"
    print(answer)
    print(answer1)
f.close()