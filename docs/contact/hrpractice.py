def numberandtimes(n, k):
    # Create a string by repeating 'n' k times
    superstring = str(n) * k
    # Convert the repeated string into a list of integers (digits)
    supernumbers = [int(digit) for digit in superstring]
    
    # Recursively sum the digits
    return recursive_sum(supernumbers)

def recursive_sum(numbers):
    # Base case: if the list is empty, return 0
    if len(numbers) == 0:
        return 0
    else:
        # Sum the first digit and the result of the recursive call on the rest of the list
        return numbers[0] + recursive_sum(numbers[1:])

# Call the function with the desired arguments
print(numberandtimes(123, 3))
