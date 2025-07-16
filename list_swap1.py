ca = [10,11]
print("ca[0]값:",ca[0],end=",")
print("ca[1]값:",ca[1])

temp = ca[0]
ca[0] = ca[1]
ca[1] = temp
print("ca[0]값:", ca[0],end=",")
print("ca[1]값:",ca[1])

print("------------")

def funca(na,nb):
    temp = na
    na =  nb
    nb = temp

ca = [10,11]
print("ca[0]값:", ca[0],end=",")
print("ca[1]값:",ca[1])
funca(ca[0],ca[1])
print("ca[0]값:", ca[0],end=",")
print("ca[1]값:",ca[1])

print("------------")
ca = [10,11]
cb = ca
print("ca값:",ca)
print("cb값:",cb)
print("ca id값:",id(ca))
print("cb id값:",id(cb))
ca[0] = 20
print("ca[0] id값:",id(ca[0]))
print("cb[0] id값:",id(cb[0]))

#얕은 복사 : 객체(리스트변수, cb)는 새로 생성,
#   하위 객체(리스트내 인덱스변수 cb[0]) 원본과 같은 참조를 가짐

print("--------------------------")
ca = [10,11]
cb = ca
print("ca값:",ca)
print("cb값:",cb)
temp = cb[0]
cb[0] = cb[1]
cb[1] = temp
print("ca값:",ca)
print("cb값:",cb)
print("ca[0]값:",ca[0],"ca[1]값:",ca[1])
print("cb[0]값:",cb[0],"cb[1]값:",cb[1])

print("---------------------------")
def funca(cb):
    temp = cb[0]
    cb[0] =  cb[1]
    cb[1] = temp

ca = [10,11]
print("ca[0]값:", ca[0],end=",")
print("ca[1]값:",ca[1])
funca(ca)
print("ca[0]값:", ca[0],end=",")
print("ca[1]값:",ca[1])

print("---------------------------")
a = [10,11,12,13]
print("리스트 a값:",a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
a[1] = 21
print("리스트 a값:",a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
b = a
print("리스트 b값:",b)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))
b = [30,31,32,33]
print("리스트 b값:",b)
print("리스트 a값:",a)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))

# 깊은 복사 : 객체(변수)뿐 아니라, 하위 객체도 새로 복사
#   복사된 객체는 원본과 독립적

print("---------------------")
#리스트를 return하는 함수 예제 프로그램
def fk(cb):
    total = 0
    for sb in range(0,3,1):
        total = total + cb[sb]
    cb[2] = total
    return cb
ca = [10,20,30]
print(ca)
cd = fk(ca)
print(ca)
print(cd)