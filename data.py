from enum import Enum


class InputData:
    POSITIVE = "1"
    NEGATIVE = "0"

    def __init__(self):
        self.result = None  # type: int
        self.outlook = None  # type: Outlook
        self.temperature = None  # type: Temperature
        self.humidity = None  # type: Humidity
        self.wind = None  # type: Wind

    def read(filename):
        arr = []  # type: list[InputData]

        with open(filename) as input:
            for line in input:
                values = line.split()
                data = InputData()
                data.result = int(values[0])
                data.outlook = Outlook(values[1])
                data.temperature = Temperature(values[2])
                data.humidity = Humidity(values[3])
                data.wind = Wind(values[4])
                arr.append(data)
        return arr



class Outlook(Enum):
    SUNNY = "sunny"
    OVERCAST = "overcast"
    RAIN = "rain"


class Temperature(Enum):
    HOT = "hot"
    MILD = "mild"
    COOL = "cool"


class Humidity(Enum):
    HIGH = "high"
    NORMAL = "normal"


class Wind(Enum):
    WEAK = "weak"
    STRONG = "strong"
