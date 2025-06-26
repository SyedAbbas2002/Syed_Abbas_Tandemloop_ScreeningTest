# Simple Calculator using Class

class Calculator:
    # Perform basic operations based on the given type
    def operate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b != 0:
                return a / b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

# Example usage
calc = Calculator()
result = calc.operate(15, 8, "add")
print("Result:", result)
