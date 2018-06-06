# ii.	Ask users to enter a number n, then print n x n 1’s and 0’s, consecutively

n = int(input("Please input an even number"))
half_n = int(n/2)
if n % 2 == 0:
    print("You input ",n)
else:
    print("You must input an even number")


for i in range(1,half_n+ 1):
    for j in range(1, half_n + 1):
        print("1 0", end="\t")
    print()
