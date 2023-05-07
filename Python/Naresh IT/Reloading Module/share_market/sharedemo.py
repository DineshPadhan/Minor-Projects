import share,time, importlib
def disshare(d):
    print("="*30)
    print("\tName\t\t\tPrice")
    print("="*30)
    for x,y in d.items():
        print("\t{}\t\t\t\t{}".format(x,y))
        print("-"*30)

d = share.shareinfo()
disshare(d)
print("I am going to sleep")
time.sleep(10)
print("I am slept")

importlib.reload(share)
d = share.shareinfo()
disshare(d)
