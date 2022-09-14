def printn(n):
    if n<=0:
        return
    else:
        print(n, end=" ")
        printn(n-1)

printn(5)
