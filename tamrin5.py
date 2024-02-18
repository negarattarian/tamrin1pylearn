import math
while("true"):

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))


    bmi = weight / math.pow(height, 2)


    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Normal weight")
    elif 25 <= bmi <= 29.9:
        print("Overweight")
    elif 30 <= bmi <= 34.9:
        print("Obesity")
    elif 35 <= bmi <= 39.9:
        print("Extreme obesity")
    else:
        print("Very extreme obesity")