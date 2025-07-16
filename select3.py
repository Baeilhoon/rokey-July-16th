# # select2.py 선택정렬

# ca = [21, 10, 11, 15, 13]
# mina = ca[0]        #21
# minix = 0           # list 내 최소값 위치

# for sb in range(1,5,1):         # 1, 2 3 4
#     if mina > ca[sb]:   
#         mina = ca[sb]   # 10
#         minix = sb      # 1

# # 첫번째 값과 최소값을 스왑
# temp = ca[0]
# ca[0] = ca[minix]
# ca[minix] = temp

# print(ca)

# # 1차 목표 ca = [10 ,21, 11, 15, 13]
# print("-------------------")

# mina = ca[1]        #21
# minix = 1           # list 내 최소값 위치

# for sb in range(2,5,1):         # 1, 2 3 4
#     if mina > ca[sb]:   
#         mina = ca[sb]   #10
#         minix = sb      #1

# # 첫번째 값과 최소값을 스왑
# temp = ca[1]
# ca[1] = ca[minix]
# ca[minix] = temp

# print(ca)

# # 2차 목표 ca = [10 ,11, 21, 15, 13]

# print("------------------------")
# mina = ca[2]        #21
# minix = 2           # list 내 최소값 위치

# for sb in range(3,5,1):         # 1, 2 3 4
#     if mina > ca[sb]:   
#         mina = ca[sb]   #10
#         minix = sb      #

# # 첫번째 값과 최소값을 스왑
# temp = ca[2]
# ca[2] = ca[minix]
# ca[minix] = temp

# print(ca)

# # 3차 목표 ca = [10 ,11, 13, 15, 21]


print("----------------------")

ca = [21, 10, 11, 15, 13]

for i in range(0,4,1):
    mina = ca[i]
    minw = i

    for sb in range(i+1,5,1):
        if mina > ca[sb]:
            mina = ca[sb]
            minw = sb

    temp = ca[i]
    ca[i] = ca[minw]
    ca[minw] = temp

print(ca)