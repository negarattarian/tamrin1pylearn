import math
while True:
    weight=float(input("enter your weighth in kg:"))
    height=float(input("enter your heighth in m :"))


    BMI=weight/math.pow(height,2)
    if BMI<18.5:
        print("underweight")
    elif 18.5 <= BMI <= 24.9:
            print("Normal weight")
    elif 25 <= BMI <= 29.9:
            print("Overweight")
    elif 30 <= BMI <= 34.9:
            print("Obesity")
    elif 35 <= BMI <= 39.9:
            print("Extreme obesity")
    else:
            print("Severe obesity")


        