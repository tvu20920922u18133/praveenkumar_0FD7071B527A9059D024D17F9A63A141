def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Get user input
num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is {factorial_recursive(num)}")
