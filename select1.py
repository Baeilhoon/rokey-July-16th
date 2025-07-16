# select1.py 선택정렬

ca = [21, 10, 11, 15, 13]
mina = ca[0]        #21
minix = 0           # list 내 최소값 위치

for sb in range(1,5,1):         # 1, 2 3 4
    if mina > ca[sb]:   
        mina = ca[sb]   #10
        minix = sb      #1

# 첫번째 값과 최소값을 스왑
temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp

print(ca)

# 1차 목표 ca = [10 ,21, 11, 15, 13]