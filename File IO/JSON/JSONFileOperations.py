#JSON_object = '{
#                 "name": "Bob", 
#                 "languages": ["Python", "Java"]
#               }'

import json
#Reading json file
with open('person.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)


#Convert dict to json
person_dict = {'name': 'Suraj',
'age': 25,
'Education': 'Engineering'
}
person_json = json.dumps(person_dict)
# Output: {"name": "Suraj", "age": 25, "Education": Engineering}
print(person_json)


#write to json file
person_dict = {"name": "Vijay",
"languages": ["English", "Hindi","Kannada","Marathi"],
"married": False,
"age": 23
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)

#printing json object
print(json.dumps(person_dict, indent = 4, sort_keys=True))