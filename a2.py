"""Create a Python Function to perform a calculation based on the following mathematical function
i=n
∑ 1 / (xi)
i=1
Do not use the Math library to perform this task. Perform this task using two different methods. One of
the methods should be using recursion.
"""

def p1(x,n):
    t=0
    for i in range(1,n+1):
        t=t+(1/(x**i))
    return t

x=int(input("Enter the value of X "))
n=int(input("Enter the value of n "))
s=p1(x,n)
print(s)
