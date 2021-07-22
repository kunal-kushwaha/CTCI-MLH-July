n = 80
hm = {}

def fibo(n):
    if n < 2:
        return n

    if n in hm:
        return hm[n]
    hm[n] = fibo(n-1) + fibo(n-2)
    return hm[n]

print(fibo(n))