import json

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_string = '{"name": "mersi", "age": "29"}'

person_dict = json.loads(person_string)
person_object = Person(**person_dict)

print(person_object)

print('The name is: ' + person_object.name)

print('The age is: ' + person_object.age)