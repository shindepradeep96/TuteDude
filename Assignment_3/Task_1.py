n = int(input("Enter a number: "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
fact = factorial(n)
print("Factorial of " +str(n)+ " is:",fact)