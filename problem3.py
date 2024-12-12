#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is negtative then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
mylist = []
for i in range(0,10):
    num = int(input("Enter a positive integer: "))
    if num < 0:
        break
    else:
        mylist.append(num)
mylist.sort()
print(f"The largest number you entered was {mylist[-1]}")

