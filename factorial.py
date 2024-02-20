def factorial(num):
    if (num == 1):
        return 1
    return num * factorial(num-1)

n = int(input("enter the num: "))
result = factorial(n)
print("The factorial of",n,"is",result)
