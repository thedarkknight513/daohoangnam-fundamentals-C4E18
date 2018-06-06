# ii.	Ask user to enter a number n, then print n x n numbers, following multiplication table pattern:

n = int(input("Please input n"))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end="\t")
    print()