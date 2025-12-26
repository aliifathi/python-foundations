# Session 5: Core Patterns (count, collect, find first, find last)

def count_greater_than(numbers, threshold):
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count

def get_greater_than(numbers, threshold):
    result = []
    for n in numbers:
        if n > threshold:
            result.append(n)
    return result

def find_first_greater_than(numbers, threshold):
    for n in numbers:
        if n > threshold:
            return n
    return None

def find_last_greater_than(numbers, threshold):
    found = None
    for n in numbers:
        if n > threshold:
            found = n
    return found


# Tests
numbers = [1, 3, 4, 7, 9]
threshold = 5

print("Numbers:", numbers)
print("Threshold:", threshold)

print("Count > threshold:", count_greater_than(numbers, threshold))
print("All > threshold:", get_greater_than(numbers, threshold))
print("First > threshold:", find_first_greater_than(numbers, threshold))
print("Last > threshold:", find_last_greater_than(numbers, threshold))

