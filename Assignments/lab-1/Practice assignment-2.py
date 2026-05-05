import math

n = int(input("Enter a number: "))

if 0 <= n <= 9:
    print("Square:", n**2)
elif 10 <= n <= 99:
    print("Square Root:", math.sqrt(n))
elif 100 <= n <= 999:
    print("Cube Root:", n ** (1/3))
else:
    print("Number not in range")
