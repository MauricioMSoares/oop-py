from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get("/api/hello")
def hello_world():
    '''
    Hello World endpoint
    '''
    return {"Hello": "World"}


@app.get("/api/restaurants/")
def get_restaurants(restaurant: str = Query(None)):
    '''
    Restaurant menu's endpoint
    '''

    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if restaurant is None:
            return {"Data": data}

        restaurant_data = []
        for item in data:
            if item["Company"] == restaurant:
                restaurant_data.append(
                    {
                        "item": item["Item"],
                        "price": item["price"],
                        "desc": item["description"],
                    }
                )
        return {"Restaurant": restaurant, "Menu": restaurant_data}

    else:
        return {"Error": f"{response.status_code} - {response.text}"}
