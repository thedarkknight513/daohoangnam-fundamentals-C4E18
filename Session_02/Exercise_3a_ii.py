# ii.	Ask users to enter a number, then print n positive numbers from 0 to n-1:     


n = int(input("Please input n"))

if n >= 0:
    for i in range(n):
         print(i, end=" ")
else:
    print("n must be a positive number")