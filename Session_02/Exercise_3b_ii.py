# ii.	Ask users to enter a number n, then print n 1’s and 0’s in total consecutively:

n = int(input("Please input n"))

for i in range(n+1):
    print("1 0", end=" ")