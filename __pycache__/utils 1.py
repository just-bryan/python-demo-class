import requests
BASE_URL = "http://fakestoreapi.com"
ENDPOINTS = {
    "PRODUCTS": "/PRODUCTS",   
    "categories": "/products/categories"
}
def get_products():
    url = BASE_URL +ENDPOINTS["PRODUCTS"]
    return requests.get(url=url).json()[:11]



def get_categories():
    url = BASE_URL +ENDPOINTS["categories"]
    return requests.get(url).json



if __name__ == '__main__':
    get_categories()
