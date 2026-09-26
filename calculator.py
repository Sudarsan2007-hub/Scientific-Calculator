import math
def sum (a,b):             #function to add
    print("Result=",a+b)

def subtraction (a,b):     #function to subtract
    print("Result=",a-b)

def multiplication (a,b):  #function to multiply
    print("Result=",a*b)

def division(a,b):         #function to divide
    print("Result=",a/b)

def power (a,b):           #function for power
    print("Result=",a**b)

def root(a,b):             #function for root
    print("Result=",a**(1/b))

def logarithm(a):            #function for log
    print("Result=",math.log10(a))
def sine(angle):
    print("sin",angle,"=",math.sin(math.radians(angle)))
def cosine(angle):
    print("cos",angle,"=",math.cos(math.radians(angle)))
def tangent(angle):
    print("tan",angle,"=",math.tan(math.radians(angle)))
def factorila(num):
    if num<0:
        print("Error")
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print("factorial of",num,"=",fact)

def percentage(a,b):
    print((a*b)/100)

print("======= SCIENTIFIC CALCULATOR =======")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square root")
print("7. Logarithm")
print("8. sine")
print("9. Cosine")
print("10. Tangent")
print("11.Factorial")
print("12. Percentage")

while True:
    ch=input("Do you want to continue with the calculator(y/n):")
    if ch=="n":
        print("calculator closed")
        break
    elif ch=="y":
        choice=input("Enter your choice:")
        list=["1","2","3","4","5","6","7","8","9","10","11","12"]
        if choice not in list:
            print("not valid ")

        elif choice == "1":
            x=float(input("Enter the first number:"))
            y=float(input("Enter the second number:"))
            sum(x,y)
        elif choice == "2":
            x=float(input("Enter the first number:"))
            y=float(input("Enter the second number:"))
            subtraction(x,y)
        elif choice == "3":
            x=float(input("Enter the first number:"))
            y=float(input("Enter the second number:"))
            multiplication(x,y)
        elif choice =="4":
            x=float(input("Enter the first number:"))
            y=float(input("Enter the second number:"))
            if y == 0:
                print("Error:cannot divide by zero")
            else:
                division(x,y)
        elif choice == "5":
            x=float(input("Enter the number:"))
            y=float(input("Enter the power :"))
            power(x,y)
        elif choice == "6":
            x=float(input("Enter the number:"))
            y=float(input("Enter the number you want to root :"))
            root(x,y)
        elif choice == "7":
            x=float(input("Enter the number:"))
            if x>0:
                logarithm(x)
            else:
                print("Error: Number must be positive")
        elif choice == "8":
            x=int(input("sin "))
            sine(x)
        elif choice == "9":
            x=int(input("cos "))
            cosine(x)
        elif choice == "10":
            x=int(input("tan "))
            tangent(x)
        elif choice== "11":
            x=int(input("Enter a positive integer:"))
            factorila(x)
        else: 
            x=int(input("Enter the number :"))
            y=int(input("Enter the percentage value:"))
            percentage(x,y)
    else:
        print("Error")
        break





    

