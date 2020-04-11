
import requests
import json
import os

#url = 'http://dummy.restapiexample.com/api/v1/employees'
#url = 'http://localhost/index.html'
#url = 'https://jsonplaceholder.typicode.com/todos/1' 
#url = 'http://api.open-notify.org/astros.json'

item = 100001498

url = 'https://sit-api.morrisons.com/productsupplier/v1/items/' + str(item) + '/suppliers?apikey=hSa6mG9aG7qd5oZ2Fw8Q06ptjEMetTk2'
print(url)

#headers = {'content-type': 'application/json', 'cache-control': 'no-cache'}
#headers = {'content-type': 'application/json'}

headers = {'content-type': 'application/json','authorization': 'Basic aFNhNm1HOWFHN3FkNW9aMkZ3OFEwNnB0akVNZXRUazI6RGRjSkltVWluZzEwZXRTdQ==','cache-control': 'no-cache'}

#response = requests.get(url)
response = requests.get(url, headers=headers)
data = response.json()
print(data)
print(type(data))
print(data['itemSuppliers'])
print(type(data['itemSuppliers']))

for i in data['itemSuppliers']:
    print(i)
    print(type(i))
    print(i['primaryInd'])
    if i['primaryInd']:
        print(i['supplierId'], ':', i['primaryInd'])

