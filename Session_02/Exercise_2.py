# Asks users enter a number n and then calculates factorial of n: (1 * 2 * 3 *... *n)

n = int(input("Please input n"))

factorial = 1

for i in range(1,n+1):
    factorial = factorial * i
print(factorial)