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

# [1,2,3,4,5,6,7]

if len(numbers) % 2 == 0:
    median1 = numbers[len(numbers)//2]
    median2 = numbers[len(numbers)//2 - 1]
    median = (median1 + median2)/2
    print(median)

else:
    median = numbers[len(numbers)//2]
    print(median)
