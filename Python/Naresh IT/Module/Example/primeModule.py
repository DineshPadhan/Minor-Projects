def primenumber(x):
    count = 0
    if x>1:
        for i in range(1,x+1):
            if x%i == 0:
                count = count+1
    if count ==2:
        return "a Prime"
    else:
        return "Not a Prime"