# Aerospace Session A1: Patterns (Counter, Filter, Find First)
# Goal: learn patterns using flight-style data

def count_above_limit(values, limit):
    """Return how many values are above a limit."""
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count

def filter_above_limit(values, limit):
    """Return a list of all values above a limit."""
    result = []
    for v in values:
        if v > limit:
            result.append(v)
    return result

def find_first_above_limit(values, limit):
    """Return the first value above a limit, or None if not found."""
    for v in values:
        if v > limit:
            return v
    return None


# Example aerospace-style data (altitude in feet, speed in knots)
altitudes_ft = [9500, 9800, 10200, 11000, 10800, 9900]
speeds_kt = [220, 240, 255, 248, 260, 235]

alt_limit = 10000
speed_redline = 250

print("Altitudes (ft):", altitudes_ft)
print("Speeds (kt):", speeds_kt)

# Pattern 1: Counter
print("How many altitudes above 10,000 ft?:", count_above_limit(altitudes_ft, alt_limit))

# Pattern 2: Filter list
print("Speeds above redline:", filter_above_limit(speeds_kt, speed_redline))

# Pattern 3: Find first
print("First altitude above 10,000 ft:", find_first_above_limit(altitudes_ft, alt_limit))

