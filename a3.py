"""
Write a Python Code that takes input as the values of x, y, a, b to solve the following equation:
[ {x + (1/y) }a * {x – (1/y)}b] / [ {y + (1/x) }a * {y – (1/x)}b]
"""

x=int(input("Enter the value of x "))
y=int(input("Enter the value of y "))
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
t1=(x+(1/y))**a
t2=(x-(1/y))**b
t12=t1*t2
t3=(y+(1/x))**a
t4=(y-(1/x))**b
t34=t3*t4
t=t12/t34
print("The value of the equation is ",t)
