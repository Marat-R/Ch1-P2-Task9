num = int(input("Number: "))

factorial = 1

if num < 0:
    print("Can't use 0 for factorial")
elif num == 0:
    print("Factorial of ", num, "is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of", num, " is ", factorial)
