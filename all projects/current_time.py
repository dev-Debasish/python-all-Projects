import time
name = input("Enter Your Name: ")
timeStamp = time.strftime("%H:%M:%S")
print(timeStamp)
hour = int(time.strftime("%H"))
if (hour >= 5 and hour < 10):
    print("Good Morning",name)
elif hour >= 10 and hour < 16:
    print("Good Noon",name)
elif hour >= 16 and hour < 19:
    print("Good AfterNoon",name)
elif hour >= 19 and hour < 21:
    print("Good Evening",name)
else:
    print("Good Night",name)


