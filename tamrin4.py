import math

weight=float(input("enter your weighth in kg:"))
height=float(input("enter your heighth in m :"))


BMI=weight/math.pow(height,2)
if BMI<18.5:
    print("underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("normal weight")
elif BMI>=25 and BMI<=29.9:
    print("over weight")
elif BMI>=30 and BMI<=34.9:
    print("obecity")
elif BMI>=35 and BMI<=39.9:
    print(" extreamobecity")




    