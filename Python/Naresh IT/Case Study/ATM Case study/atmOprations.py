import atmExceptions as ae

bal = 500
def deposit():
    damt = int(input("Enter Your Deposit Amount: "))
    if damt<=0:
        raise ae.depositError
    else:
        global bal
        bal +=damt
        print("Your account xxxxx123 credit with INR {}".format(damt))
        print("Your Balance xxxxx123 is INR {}".format(bal))
def withdraw():
    global bal
    wamt = int(input("Enter Your Withdraw Amount: "))
    if wamt<=0:
        raise ae.withdrawError
    elif wamt > bal:
        raise ae.insufficientFundError
    else:
        # global bal
        bal -=wamt
        print("Your account xxxxx123 debited with INR {}".format(wamt))
        print("Your Balance xxxxx123 is INR {}".format(bal))

def balenq():
    print("Your Balance xxxxx123 is INR {}".format(bal))