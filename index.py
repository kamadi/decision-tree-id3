from data import InputData, Outlook, Temperature, Humidity, Wind
from node import NodeCreator
from pprint import pprint


def create_child_node(node):
    for child in node.children:
        child_node = NodeCreator.create_node(child.arr)
        if child_node.result is not None:
            child.result = child_node.result
        else:
            child.children.append(child_node)

        for item in child.children:
            create_child_node(item)


def test(node, item):
    if node.result is not None:
        # pprint(vars(item))
        return node.result
    else:
        for child in node.children:
            if child.data is not None:
                if (child.type == Outlook and child.data == item.outlook) \
                        or (child.type == Temperature and child.data == item.temperature) \
                        or (child.type == Humidity and child.data == item.humidity) or \
                        (child.type == Wind and child.data == item.wind):
                    return test(child, item)
            else:
                for child_node in child.children:
                    return test(child_node, item)


arr = InputData.read("input.txt")

node = NodeCreator.create_node(arr)

print(node)
create_child_node(node)
print(node)

test_data = InputData.read("test.txt")

for item in test_data:
    print(test(node, item))
