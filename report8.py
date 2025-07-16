# # report8.py

# # 문제3번
# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0]
# print(arr)

# print("------------------")

# # 문제4번
# a = [1, 2, 3]
# b = a
# print(id(a) == id(b))

# print("------------------")

# # 문제5번
# x = 42
# y = 42
# print(id(x) == id(y)) #256까지의 숫자는 보통 True

# a = 10000
# b = 10000
# print(id(a) == id(b)) #True // “10000”이라는 리터럴은 같은 코드 블록 안에 한 번만 상수 테이블(constant pool)으로 들어감 // False가 나올수도있음

# # **리터럴 풀링(또는 상수 풀링, constant pooling)**은 
# # 파이썬 컴파일러가 “소스 코드에 등장한 동일한 리터럴(상수 값)”을 한 번만 메모리(Constant Pool)에 올려두고, 
# # 이후에는 그걸 재사용하도록 최적화하는 기법이에요.

# x = int("42")
# y = 42
# print(id(x) == id(y)) #True

# a = int("10000")
# b = int("10000")
# print(id(a) == id(b)) #False 

# print("-----------------------")
# # 문제6번
# a = [10, 20, 30]
# b = a.copy()
# print(a)
# print(b)

# import copy

# orig = [1, [2, 3]]
# shallow = copy.copy(orig)
# deep    = copy.deepcopy(orig)

# # 내부 리스트를 바꿔볼 때
# shallow[1].append(99)
# print(orig)   # [1, [2, 3, 99]]  ← 얕은 복사본이 건드린 결과가 원본에 반영

# deep[1].append(42)
# print(orig)   # [1, [2, 3, 99]]  ← 깊은 복사본은 원본과 완전 분리

# #문제7번
# print("-----------------")
# a = []

# for i in range(5):
#     num = int(input("5개의 숫자를 입력해주세요:"))
#     a.append(num)
# print(a)
# max = a[0]

# for j in range(1,len(a),1):
#     if max < a[j]:
#         max = a[j]

# print(max)

# # 문제10번
# print("-----------------")

a = { 'a': 10, 'b': 20, 'c': 30 }
def sum(x):
    print(x['a']+x['b']+x['c'])
sum(a)