import json
import xml.etree as ET
import yaml
from dataclasses import dataclass, asdict

@dataclass
class xmlStruct:
    def __inti__(self, structType: str, struct: str):
        self.structType = "xml"
        self.struct = struct
        self.elements = self.element_counter(self, struct) # number of discrete elements
        self.tree_depth = self.tree_depth(self, struct) # Maxmimum discrete element depth
        self.attributes = self.contains_attributes(self, struct) # Does the structure implement attributes
        self.namespacing = self.uses_namespaces(self, struct) # Does the structure implement namespacing

    def __str__(self) -> str:
        return f'{self.type} field containing {self.elements} discrete elements'

    def __repr__(self) -> str:
        return f'{type(self)}.__name__'


    
    # Methods
    def element_counter(self, struct):
        root = ET.fromstring(struct)
        
        def recursive_count(element):
            if len(element) == 0:
                return 1
            else:
                count = 0
                for child in element:
                    count += count_recursively(child)
            return count
            
        return count_recursively(root)
    
    def tree_depth(self, struct):
        root = ET.fromstring(struct)
        
        def recursive_depth_search(element, current_depth):
            #if element has no children, return current depth
            if len(element) == 0:
                return current_depth
            else:
                return max(recursive_depth_search(child, current_depth + 1) for child in element)
    
    return recursive_depth_search(root, 1)

    def contains_attributes(self, struct):
    root = ET.fromstring(struct)

    def check_attributes_recursively(element):
        # If the element has attributes, return True
        if element.attrib:
            return True
        # Check each child element recursively
        for child in element:
            if check_attributes_recursively(child):
                return True
        return False

    return check_attributes_recursively(root)

    def uses_namespaces(self, struct):
    root = ET.fromstring(self, struct)

    def check_namespaces_recursively(element):
        # Check if the element has any namespace attributes
        for attrib in element.attrib:
            if attrib.startswith('xmlns'):
                return True
        
        # Recursively check each child element
        for child in element:
            if check_namespaces_recursively(child):
                return True
        
        return False

    return check_namespaces_recursively(root)


    def to_json(self, struct):
        """Convert the data class into a JSON string"""
        return json.dumps(asdict(self))

    def to_yaml(self, struct): 






@dataclass
class ymlStruct:
    def __init__(self, type):
        self.type = "yaml"








@dataclass
class jsonStruct:
    def __init__(self, type):
        self.type = "json"
