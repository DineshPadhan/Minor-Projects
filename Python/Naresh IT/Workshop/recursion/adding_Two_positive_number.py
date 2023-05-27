def dosum(m,n):
    if (n == 0):
        return m
    else:
        m = m + 1
        n = n - 1
        print("m = ",m)
        print("n = ",n)
        return (dosum(m,n))
print("Sum is ", dosum(3,4))