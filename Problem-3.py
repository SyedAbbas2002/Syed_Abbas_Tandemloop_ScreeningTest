# Generate a series of odd numbers based on the given input

# Take input from the user
a = int(input("Enter a: "))

# If the number is even, subtract 1 to make it odd
if a % 2 == 0:
    a -= 1

# Create a list of odd numbers: 1, 3, 5, ... up to the adjusted value
output = [2 * i + 1 for i in range((a + 1) // 2)]

# Print the numbers as a comma-separated string
print(", ".join(map(str, output)))
