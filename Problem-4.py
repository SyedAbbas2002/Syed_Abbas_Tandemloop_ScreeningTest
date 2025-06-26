# Count how many numbers in the list are divisible by 1 to 9

# Given list of numbers
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Create a dictionary to store counts for numbers divisible by 1 to 9
result = {i: 0 for i in range(1, 10)}

# Check each number for divisibility from 1 to 9
for num in numbers:
    for i in range(1, 10):
        if num % i == 0:
            result[i] += 1

# Print the final result
print(result)
