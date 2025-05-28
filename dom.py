from enum import Enum

class Node:
    def __init__(self):
        pass

class NodeType(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

class Text(NodeType):
    def __init__(self, text):
        super().__init__(text)

class Element(NodeType):
    def __init__(self, element):
        super().__init__(element)

class ElementData:
    def __init__(self, tag_name: str, attributes: dict[str, str] = {}):
        self.tag_name = tag_name
        self.attributes = attributes


def text_constructor(text: str) -> Text:
    return Text(text)

def element_constructor(tag_name: str, attributes: dict[str, str] = {}) -> Element:
    return Element(ElementData(tag_name, attributes))

