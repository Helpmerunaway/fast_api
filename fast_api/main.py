from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

from enum import Enum


class ModelName(str, Enum):
	alexnet = 'alexnet'
	resnet = 'resnet'
	lenet = 'lenet'


app = FastAPI()


class Item(BaseModel):
	name: str
	price: float
	is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
	return {"Hello, world!"}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
	if model_name is ModelName.alexnet:
		return {"model_name": model_name, "message": "Deep Learning FW!"}

	if model_name.value == 'lenet':
		return {"model_name": model_name, "message": 'LeCNN all the images'}

	return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/items/{items_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}


@app.post("/items/{items_id}")
def post_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
	return {"item_name": item.name, "item_id": item_id}


@app.delete("/items/{items_id}")
def delete_item(item_id: int):
	return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
	return {"user_id": "the current user"}


@app.get("/users/{users_id}")
async def read_user(user_id: str):
	return {"user_id": user_id}


@app.get("/users")
async def read_users():
	return ["Rick", "Morty"]


userList = ['Spike', 'Jet', 'Ed', 'Faye', 'Ein']


@app.get('/userlist')
async def userlist_(start: int = 0, limit: int = 10):
	return userList[start:start+limit]