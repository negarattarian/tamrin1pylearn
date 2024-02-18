import math
for i in range(1000):
    print("welcome to my calculator")
    print("+")
    print("-")
    print("*")
    print("/")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("factorial")
    print("log")
    print("sqrt")
    print()
    print("exit")
    op=(input("enter your operator:"))
    if op=="exit":
        print("byebye")
        break
    if op=="+" or op=="-" or op=="*" or op=="/":
        a=float(input("num1:"))
        b=float(input("num2:"))
    elif op=="tan" or op=="cot" or op=="sin" or op=="cos":
        a=float(input("num1:"))
        x=(a*180)/(math.pi)
        print("zaviye be darage :",x)
    else:
        a=float(input("num1:"))
       
        

    if op=="+":
        result=a+b
    elif op=="-":
        result=a-b
    elif op=="*":
        result=a*b
    elif op=="/":
        if b==0:
            result="can not devide by zero"
        else:
            result=a/b
    elif op=="sin":
        
        result=math.sin(a)
    elif op=="cos":
        
        result=math.cos(a)
    elif op=="tan":
       
        result=math.tan(a)
    elif op=="cot":
        
        result=math.cos(a)/math.sin(a)
    elif op=="factorial":
        result=math.factorial(int(a))
    elif op=="sqrt":
        result=math.sqrt(a)
    elif op=="log":
        result=math.log(a)
    elif op=="exit":
        break
    print("result is ",result)
