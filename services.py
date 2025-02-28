import requests
from utils.env import BASE_URL

def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)

def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)




def getCategory():
    url = f"{BASE_URL}/category/"
    respose = requests.get(url)
    if respose.status_code == 200:
        data = respose.json()
        return data
    else:
        print(respose.status_code)


def getProduct(category):
    url = f"{BASE_URL}/products/?category={category}"
    respose = requests.get(url)
    print(respose.status_code)
    if respose.status_code == 200:
        data = respose.json()
        return data
    else:
        print(respose.status_code)


def getProductDetail(product_name):
    url = f"http://127.0.0.1:8000/api/v1/products/{product_name}/"
    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(response.status_code)
    except Exception as e:
        return e


def createCartUser(cart):
    url = f"{BASE_URL}/cart/create/"
    response = requests.post(url, json=cart)
    
    if response.status_code == 200 or 201:
        data = response.json()
        return data
    else:
        print(response.status_code)


def getUserCart(user_id):
    url = f"{BASE_URL}/cart/get/{user_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        
        
        
        
        


