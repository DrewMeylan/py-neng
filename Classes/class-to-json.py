'''
def to_dict(obj: Any) -> Any
    """Convert class object and its members to dictionary.
       Each class member is treated as an element to the current dictionary field.
       Each member object is treated as a sub dictionary.
       Each List[Any] is treated as a new list of dictionaries.
    """
    if isinstance(obj, dict):
        raise Exception("Dictionary type is not supported.")

    data = {}
    tags = {}

    subelements = {} # type: Dict[Any, Any]
    for member in get_members(obj):
        item = getattr(obj, member)
        member = member.replace('_', '-')


        # if object is None, add empty tag
        if item is None:
            subelements[member] = {member:None}
        else:
            if not isinstance(item, (str, XmlElement, list, set, tuple)):
                raise Exception("Attributes must be an expected type, but was: {}.".format(type(item)))


            # Add list sub-elements
            if isinstance(item, (list, set, tuple)):
                subelements[member] = []
                for list_object in item:
                    subelements[member].append(to_dict(list_object))
            # Add sub-element
            elif isinstance(item, XmlElement):
                subelements[member] = to_dict(item)
            # Add element's tag name
            else:
                tags[member] = item

    try:
        if obj._NAME:
            data.update(tags)
        else:
            raise Exception("Name attribute can't be empty.")
    except (AttributeError, TypeError) as ex:
        print("Attribute value or type is wrong. %s: %s", obj, ex)
        raise

    # Add sub elements if any
    if subelements:
        for name, values in subelements.items():
            sub = {} # type: Dict
            if isinstance(values, list): # if list of elements. Add all sub-elements
                sub[name] = []
                for value in values:
                    sub[name].append(value)
            else: # single sub-child or None
                if values is None: # if None, add empty tag with name
                    sub[name] = None
                else: # else add object
                    sub[name] = values
            data[name] = sub[name]
    try:
        if obj._TEXT:
            data[obj._NAME] = obj._TEXT
    except AttributeError as ex:
        print("Attribute does not exists. %s: %s", obj, ex)
        raise

    return data

def dict_to_json(data: dict) -> str:
    return json.dumps(data, sort_keys=True, indent=4):
'''

import json
import psycopg2
from typing import Any, List, Dict

def toJSON(classObject):
    try:
        # Convert the class instance to a JSON object
        class_json = json.dumps(classObject.__dict__)

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="netbox",
            user="netbox",
            password="netbox",
            host="localhost",  # Replace with your PostgreSQL host
            port="5432"  # Replace with your PostgreSQL port
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Insert the JSON object into the database
        cursor.execute(f"INSERT INTO your_table_name (json_data) VALUES (%s);", (class_json,))

        # Commit the transaction and close the database connection
        conn.commit()
        conn.close()

        print("Data successfully inserted into the database.")

    except Exception as e:
        print(f"Error: {str(e)}")

# Example class definition
class SampleClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example class instance
sample_instance = SampleClass("John", 30)

# Call the toJSON function to convert and export the class instance
toJSON(sample_instance)
