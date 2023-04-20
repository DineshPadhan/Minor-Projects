n=int(input("Enter The Number: "))
print("="*50)
if n<=0:
    print("{} is invalid input.".format(n))
else:
    for i in range(1,n+1):
        if n%i==0:
            print(i)
print("=" * 50)