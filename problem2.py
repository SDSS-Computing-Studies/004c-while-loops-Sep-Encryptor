#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
c=0
a=1
N=(input("enter a number: ")).strip()
N=int(N)
while a <= 12:
    c += N
    print(c,end=" ")
    a += 1
    