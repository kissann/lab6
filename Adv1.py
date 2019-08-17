#Задача 1
#Дано список країн і міст кожної країни. Потім дані назви міст. Для кожного міста вкажіть, в якій країні воно знаходиться.
st=int(input("Введите розмер словаря:"))
dict={}
answer={}
for i in range(st):
    st=list(map(str,input("Введите страну и города в ней").split(' ')))
    kl=st[0]
    del st[0]
    dict[kl]=st
kol=int(input("Введите количество запросов:"))
print("Введите города")
zap={}
for ii in range(kol):
    countr=input()
    zap[ii]=countr
for kn in zap:
    for serch in dict:
        for t in dict[serch]:
            if zap[kn]==t:
                answer[kn]=serch

print(dict)
print(zap)
for u in answer:
    print(str(answer[u]))
