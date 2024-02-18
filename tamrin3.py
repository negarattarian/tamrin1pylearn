
while("true"):
    name=input("name:")
    family=input("family:")
    a=float(input("num1:"))
    b=float(input("num2:"))
    c=float(input("num3:"))
    average=(a+b+c)/3
    if a >= 0 and b >= 0 and c >= 0:

        if average>=17:
            print("great")
        elif average<17 and average>=12:
            print("normal")
        elif average<12:
            print("failed")
    else:
        break
        