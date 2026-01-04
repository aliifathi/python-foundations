# Aerospace Session A3
# State Tracking Patterns:
# - MAX value
# - MIN value
# - LAST matching event


def get_max_altitude(flight_log):
    max_altitude = flight_log[0].get("altitude", 0)
    for dic in flight_log:
        if dic.get("altitude", 0) > max_altitude:
            max_altitude = dic.get("altitude", 0)
    return max_altitude


def get_min_fuel(flight_log):
    min_fuel = flight_log[0].get("fuel", 0)
    for dic in flight_log:
        if dic.get("fuel", 0) < min_fuel:
            min_fuel = dic.get("fuel", 0)
    return min_fuel


def get_last_critical_event(flight_log):
    last_critical = None
    for dic in flight_log:
        if dic.get("status", 0) == "CRITICAL":
            last_critical = dic
    return last_critical


# -----------------------------
# Test Data
# -----------------------------

flight_log = [
    {"altitude": 12000, "fuel": 30, "status": "OK"},
    {"altitude": 15000, "fuel": 22, "status": "WARN"},
    {"altitude": 18000, "fuel": 18, "status": "CRITICAL"},
    {"altitude": 14000, "fuel": 15, "status": "OK"},
    {"altitude": 20000, "fuel": 12, "status": "CRITICAL"}
]

print("Max altitude:", get_max_altitude(flight_log))
print("Min fuel:", get_min_fuel(flight_log))
print("Last CRITICAL event:", get_last_critical_event(flight_log))

