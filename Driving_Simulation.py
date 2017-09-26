print("Welcome to Driving Simulator")
u = 0
t = int(input("Time spent on the road :"))
a = int(input("Acceleration : "))
d = int(input("Target Distance : "))
for duration in range(0, t+1):
    distance = int(((a*duration*duration)/2))
    star = int(distance/10)
    print("Duration",duration,end="")
    print(" Distance","*" * star)

speed_limit = 60
if a*t > speed_limit:
    print("The person went over the speed limit. ","Max speed was", a*t, "m/s")
else:
    print("The person did not go over the speed limit.", "Max speed was", a*t, "m/s")

if d > distance:
    print("The person did not reach the destination.", "Reached:", distance, "m")
else:
    print("The person reached the destination.", "Reached:", distance, "m" )
