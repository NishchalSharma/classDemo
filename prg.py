#My new Python program

def f(num):
    print("hello world")
    def number(num1,num2,num3):
    if num1 >=num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(number(100,100,100))
