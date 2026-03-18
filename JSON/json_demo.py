# javascript Object Notation
import json

people_string = '''  {
    "people": [
        {
            "name": "Adeel Solangi",
            "language": "Sindhi",
            "id": "V59OF92YF627HFY0",
            "bio": "Donec lobortis eleifend condimentum. Cras dictum dolor lacinia lectus vehicula rutrum. Maecenas quis nisi nunc. Nam tristique feugiat est vitae mollis. Maecenas quis nisi nunc.",
            "version": 6.1
        },
        {
            "name": "Afzal Ghaffar",
            "language": "Sindhi",
            "id": "ENTOCR13RSCLZ6KU",
            "bio": "Aliquam sollicitudin ante ligula, eget malesuada nibh efficitur et. Pellentesque massa sem, scelerisque sit amet odio id, cursus tempor urna. Etiam congue dignissim volutpat. Vestibulum pharetra libero et velit gravida euismod.",
            "version": 1.88
        }
    ]
}
'''
# json.loads converts JSON string into python object 
data = json.loads(people_string)
print(type(data))
print(type(data['people']))


# json.dumps is used to convert python object into json 
for person in data['people']:
    del person['bio']

new_string = json.dumps(data,indent=2)
print(new_string)

# how to load json file into python 

with open('states.json') as f:
    data_json = json.load(f)

for state in data_json['states']:
    print(state['name'], state['abbreviation'])
    del state['area_codes']

with open('new_states.json','w') as f:
    json.dump(data_json, f,indent=2)


