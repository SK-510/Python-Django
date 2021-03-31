"""Write a Python function to find the next number in the series:
2, 3, 10, 15, 26, 35, 50, 63, ?"""


a=1
while a<=9:
    if a%2==1:
        q=(a**2)+1
        print(q)
    else:
        q=(a**2)-1
        print(q)
    a=a+1
print("Hence, The next value of the series will be",q) 
