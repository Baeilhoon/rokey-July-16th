#select_func.py #선택 정렬 종합

ca = [21,10,11,15,13]

def fselsort(lists):
    
    for i in range(0,len(lists)-1,1):
        mina = lists[i]
        minx = i
        for j in range(i+1,len(lists),1):
            if mina > ca[j]:
                mina = ca[j]
                minx = j
        temp = ca[i]
        ca[i] = ca[minx]
        ca[minx] = temp

    print(lists)

fselsort(ca)
print(ca)