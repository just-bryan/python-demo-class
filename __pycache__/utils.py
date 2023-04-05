#READ ON SCHEDULING TASK
import requests
BASE_URL = "https://fakestoreapi.com/"
ENDPOINTS= {
    "products":"/products",
    "categories": "/products/categories"
}


def get_products():
    url = BASE_URL + ENDPOINTS['PRODUCTS']
    return requests.get(url=url).json()[:11]

def get_categories():
    url = BASE_URL + ENDPOINTS['categories']
    return requests.get(url).json()
   

if __name__ == '__main__':
    print("hello world")
    
#    get_categories()