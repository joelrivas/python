def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

def min_sec_2_hours(minutes,seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(236))
print(seconds_to_hours(1568))
print(min_sec_2_hours(236,1568))
