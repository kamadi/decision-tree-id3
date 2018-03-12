from data import InputData, Outlook, Temperature, Humidity, Wind

from utils import calculate_entropy, calculate_total_entropy

arr = InputData.read("input.txt")

print(arr)

positive_count = 0
negative_count = 0

count_map = {}

for outlook in list(Outlook):
    count_map[str(outlook.name) + InputData.NEGATIVE] = 0
    count_map[str(outlook.name) + InputData.POSITIVE] = 0

for temperature in list(Temperature):
    count_map[str(temperature.name) + InputData.NEGATIVE] = 0
    count_map[str(temperature.name) + InputData.POSITIVE] = 0

for humidity in list(Humidity):
    count_map[str(humidity.name) + InputData.NEGATIVE] = 0
    count_map[str(humidity.name) + InputData.POSITIVE] = 0

for wind in list(Wind):
    count_map[str(wind.name) + InputData.NEGATIVE] = 0
    count_map[str(wind.name) + InputData.POSITIVE] = 0

for item in arr:
    if item.result == 1:
        positive_count += 1
    else:
        negative_count += 1

    for value in list(Outlook):
        if item.outlook == value:
            key = str(value.name) + str(item.result)
            count_map[key] = count_map[key] + 1

    for value in list(Temperature):
        if item.temperature == value:
            key = str(value.name) + str(item.result)
            count_map[key] = count_map[key] + 1

    for value in list(Humidity):
        if item.humidity == value:
            key = str(value.name) + str(item.result)
            count_map[key] = count_map[key] + 1

    for value in list(Wind):
        if item.wind == value:
            key = str(value.name) + str(item.result)
            count_map[key] = count_map[key] + 1

total = len(arr)

entropy_total = calculate_entropy(positive_count, negative_count)

ig_outlook = entropy_total

for outlook in list(Outlook):
    ig_outlook -= calculate_total_entropy(count_map[str(outlook.name) + InputData.POSITIVE],
                                          count_map[str(outlook.name) + InputData.NEGATIVE],
                                          total)

print(ig_outlook)

ig_temperature = entropy_total

for temperature in list(Temperature):
    ig_temperature -= calculate_total_entropy(count_map[str(temperature.name) + InputData.POSITIVE],
                                              count_map[str(temperature.name) + InputData.NEGATIVE],
                                              total)

print(ig_temperature)

ig_humidity = entropy_total

for humidity in list(Humidity):
    ig_humidity -= calculate_total_entropy(count_map[str(humidity.name) + InputData.POSITIVE],
                                           count_map[str(humidity.name) + InputData.NEGATIVE],
                                           total)

print(ig_humidity)

ig_wind = entropy_total

for wind in list(Wind):
    ig_wind -= calculate_total_entropy(count_map[str(wind.name) + InputData.POSITIVE],
                                       count_map[str(wind.name) + InputData.NEGATIVE],
                                       total)

print(ig_wind)
