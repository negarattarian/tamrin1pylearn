
a=float(input("zele 1:"))
b=float(input("zele 2:"))
c=float(input("zele 3:"))
while("true"):
    if a + b > c and a + c > b and b + c > a:
        print("mosalas mishe sakht")
        break
    else:
        print("ba in se zel nemishe mosalas sakht")
        a = float(input(" side 1: "))
        b = float(input(" side 2: "))
        c = float(input(" side 3: "))
