# Aerospace Session A2
# Filter + collect with multiple conditions

def get_critical_highspeed_altitudes(flight_log):
    result = []
    for dic in flight_log:
        if dic.get("status", 0) == "CRITICAL" and dic.get("speed", 0) > 600:
            result.append(dic.get("altitude", 0))
    return result


# Test data
flight_log = [
    {"altitude": 12000, "speed": 450, "status": "OK"},
    {"altitude": 15000, "speed": 520, "status": "WARN"},
    {"altitude": 18000, "speed": 610, "status": "CRITICAL"},
    {"altitude": 14000, "speed": 480, "status": "OK"},
    {"altitude": 20000, "speed": 590, "status": "CRITICAL"}
]

print(get_critical_highspeed_altitudes(flight_log))

