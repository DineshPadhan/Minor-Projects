import threading,time
def generate(n):
	print("Name of the threading generate()=",threading.current_thread().name)
	if(n<=0):
		print("{} Invalid Input".format(n))
	else:
		print("---------------------------------------------")
		print("Numbers within:{}".format(n))
		print("---------------------------------------------")
		for i in range(1,n+1):
			print("\tValue of i={}".format(i))
			time.sleep(1)
		print("---------------------------------------------")


# main program
n=int(input("Enter How Many Numbers u want to generate:"))
t1=threading.Thread(target=generate,args=(n,)) # Sub thread creation
t1.start()