def stih(str):
    str = str.split()
    list_1 = []
    for k in str:
        summa = 0
        for i in k:
            if i in 'уеыаояию':
                summa += 1
        list_1.append(summa)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if stih(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')