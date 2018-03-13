import sys

from data import InputData, Outlook, Temperature, Humidity, Wind

from utils import calculate_entropy, calculate_total_entropy


class Node(object):

    def __init__(self, type, data=None):
        self.type = type
        self.data = data
        self.children = []  # type: list(Node)
        self.arr = []
        self.result = None

    def add_child(self, value):
        self.children.append(value)

    def add_item(self, value):
        self.arr.append(value)


class NodeCreator:

    @staticmethod
    def create_node(arr):

        positive_count = 0
        negative_count = 0

        max = -sys.maxsize - 1
        max_class = None

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

        if positive_count > 0 and negative_count == 0:
            result = Node(None)
            result.result = InputData.POSITIVE
            return result

        if negative_count > 0 and positive_count == 0:
            result = Node(None)
            result.result = InputData.NEGATIVE
            return result

        total = len(arr)

        entropy_total = calculate_entropy(positive_count, negative_count)


        ig_outlook = entropy_total

        for outlook in list(Outlook):
            ig_outlook -= calculate_total_entropy(count_map[str(outlook.name) + InputData.POSITIVE],
                                                  count_map[str(outlook.name) + InputData.NEGATIVE],
                                                  total)

        # print("outlook:", ig_outlook)


        ig_temperature = entropy_total

        for temperature in list(Temperature):
            ig_temperature -= calculate_total_entropy(count_map[str(temperature.name) + InputData.POSITIVE],
                                                      count_map[str(temperature.name) + InputData.NEGATIVE],
                                                      total)

        # print("temp:", ig_temperature)


        ig_humidity = entropy_total

        for humidity in list(Humidity):
            ig_humidity -= calculate_total_entropy(count_map[str(humidity.name) + InputData.POSITIVE],
                                                   count_map[str(humidity.name) + InputData.NEGATIVE],
                                                   total)

        # print("humidity:", ig_humidity)



        ig_wind = entropy_total

        for wind in list(Wind):
            ig_wind -= calculate_total_entropy(count_map[str(wind.name) + InputData.POSITIVE],
                                               count_map[str(wind.name) + InputData.NEGATIVE],
                                               total)

        # print("wind:", ig_wind)

        if ig_outlook > max:
            max = ig_outlook
            max_class = Outlook

        if ig_temperature > max:
            max = ig_temperature
            max_class = Temperature

        if ig_humidity > max:
            max = ig_humidity
            max_class = Humidity

        if ig_wind > max:
            max = ig_wind
            max_class = Wind

        # print("max", max)
        # print("value", max_class)

        node = Node(max_class)
        node.arr = arr

        if max_class == Outlook:
            sunny_node = Node(Outlook, Outlook.SUNNY)
            overcast_node = Node(Outlook, Outlook.OVERCAST)
            runny_node = Node(Outlook, Outlook.RAIN)

            node.add_child(sunny_node)
            node.add_child(overcast_node)
            node.add_child(runny_node)

            for item in arr:
                if item.outlook == Outlook.SUNNY:
                    sunny_node.add_item(item)
                if item.outlook == Outlook.OVERCAST:
                    overcast_node.add_item(item)
                if item.outlook == Outlook.RAIN:
                    runny_node.add_item(item)

        if max_class == Temperature:
            hot_node = Node(Temperature, Temperature.HOT)
            mild_node = Node(Temperature, Temperature.MILD)
            cool_node = Node(Temperature, Temperature.COOL)

            node.add_child(hot_node)
            node.add_child(mild_node)
            node.add_child(cool_node)

            for item in arr:
                if item.temperature == Temperature.HOT:
                    hot_node.add_item(item)
                if item.temperature == Temperature.MILD:
                    mild_node.add_item(item)
                if item.temperature == Temperature.COOL:
                    cool_node.add_item(item)

        if max_class == Humidity:
            high_node = Node(Humidity, Humidity.HIGH)
            normal_node = Node(Humidity, Humidity.NORMAL)

            node.add_child(high_node)
            node.add_child(normal_node)

            for item in arr:
                if item.humidity == Humidity.HIGH:
                    high_node.add_item(item)
                if item.humidity == Humidity.NORMAL:
                    normal_node.add_item(item)

        if max_class == Wind:
            weak_node = Node(Wind, Wind.WEAK)
            strong_node = Node(Wind, Wind.STRONG)

            node.add_child(weak_node)
            node.add_child(strong_node)

            for item in arr:
                if item.wind == Wind.WEAK:
                    weak_node.add_item(item)
                if item.wind == Wind.STRONG:
                    strong_node.add_item(item)

        return node


