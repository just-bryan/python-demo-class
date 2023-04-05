import json
import requests
from pprint import pprint
data='''
[
    {"id" : "001",
     "x"  :"2",
     "name"  : "chuck"}
     
     
    {"id":"019",
    "x"  : "10",
    "name" : "benice",
    "skills":["A","B","C"]}
    
    
]'''


info = json.loads(data)
for p in info:    
    print(p)
    print (p['skills'][0]) if "skills" in p else...


BASE_ENDPOINT="http://fakestoreapi.com/"
url= "products/"
CART_ENDPOINT="carts/"

post_data ={
    "title":'benice',
    "price":1.5,
    "description": 'loran ipsum set',
    "image": 'http://i.pravatar.cc',
    "catergories":'electronic'
}
response= requests.post(url,json=post_data)
data= response.json()
pprint(data,indent=4)
# json.loads converts json to python
# json.dumps coverts python to json