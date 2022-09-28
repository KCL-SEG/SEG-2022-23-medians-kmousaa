"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numbers.sort()

# [1,2,3,4,5,6]


if (len(numbers) % 2) == 0:
    mid = int(len(numbers) / 2)
    print(numbers[mid])
else:
    lowmid = int(numbers[len(numbers)//2])
    highmid =  int(numbers[-(-len(numbers)//2)])

    print((lowmid+highmid)//2)
