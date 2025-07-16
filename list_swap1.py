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