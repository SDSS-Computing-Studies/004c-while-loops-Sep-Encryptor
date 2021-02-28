#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""


while True:
    N=input("enter a number: ")
    N=float(N)
    if N%2 != 0:
        print("That is not an even integer")
    else:
        print('That is an even integer')
        break
    
