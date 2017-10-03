temporary = 0
list = [1,0,0]
a = input()

for x in a:
    if x.upper()=="A":
        temporary = list[1]
        list[1]=list[0]
        list[0]=temporary

    elif x.upper()=="B":
        temporary = list[2]
        list[2]=list[1]
        list[1]=temporary

    elif x.upper()=="C":
        temporary = list[2]
        list[2]=list[0]
        list[0]=temporary
    else:
        print("Error")

if list[0]==1:
    print ("1")
elif list[1]==1:
    print("2")
elif list[2]==1:
    print("3")
