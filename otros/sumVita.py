
def fact(f):
    factorial = 1

    for i in range(1,f+1):
        factorial *=  i
    return factorial

def com(n, k):
    combina = fact(n)/(fact(k)*fact(n-k))
    return combina

def sum(n, k):
    suma = 0
    for i in range(k+1):
        if i % 2 == 0:
            suma += com(n,i)
    return suma

n, k = map(int, raw_input().strip().split())
if 0 <= n and k <=10**9:
    if n >= k:
        print (sum(n,k))
