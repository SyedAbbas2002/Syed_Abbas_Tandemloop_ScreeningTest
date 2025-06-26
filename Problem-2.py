# Generate a series of first 'a' odd numbers

# Take input from the user
a = int(input("Enter a: "))

# Create a list of odd numbers: 1, 3, 5, ...
output = [2 * i + 1 for i in range(a)]

# Print the numbers as a comma-separated string
print(", ".join(map(str, output)))
