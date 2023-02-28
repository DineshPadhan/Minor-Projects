import time
hour = time.localtime().tm_hour
if(hour>=6 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir")
elif(hour>=17 and hour <21):
    print("Good Evening Sir")
else:
    print("Good Night Sir")