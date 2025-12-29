# Session 6: Max / Min Tracking Pattern

def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value

def find_min(numbers):
    min_value = numbers[0]
    for n in numbers:
        if n < min_value:
            min_value = n
    return min_value


# Tests
numbers = [3, 7, 2, 9, 5]

print("Numbers:", numbers)
print("Max value:", find_max(numbers))
print("Min value:", find_min(numbers))

