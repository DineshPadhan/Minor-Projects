import threading,time
def generate(n):
    print("Name of the threading generate()=",threading.current_thread().name)
    

t1 = threading.Thread(target=generate, args=(1,))
t1.start()