# how to read the data from  api -- json format

import json
from urllib.request import urlopen

with urlopen('https://api.exchangerate-api.com/v4/latest/USD') as response:
    source = response.read()

data = json.loads(source)
print(json.dumps(data,indent=2))
print(data)
rates = data['rates']
print(rates.items())

# json.load -> load file as json in python
# json.loads -> load string as json in python
# json.dump -> dump json as file
# json.dumps -> dump json as string



# for sno,(currency,rates) in enumerate(rates.items()):
#     print(sno,(currency,rates))






# print(data['rates'])
# list = []
# for sno,currency in enumerate(data['rates']):
#     currency_app = '{} - {}'.format(sno,currency)
#     list.append(currency_app)
#     # print(currency,data['rates'])

# print(list)