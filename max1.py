# max1.py

su = [5, 4, 7, 10, 6]

def fmax(a,b,c,d,e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    return max

max = fmax(su[0],su[1],su[2],su[3],su[4])
print("최댓값 max:",max)