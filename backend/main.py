from typing import Optional
import requests
import json
from fastapi import FastAPI, HTTPException, Request
import os
from string import Template
import time

app = FastAPI()
url = 'https://api.plantjammer.com/graphql'
headers = {
    "Authorization": os.environ.get("API_KEY")}


@app.get("/")
def read_root():
    return {"Hello": "Adib"}


@app.get("/recipes/{keyword}")
def get_recipes(keyword: str):
    '''
    For getting the recipes based on a keyword
    '''
    # we also have serving, estimated time, and suggested ingredients
    query_template = Template(
        """query dishes {
            dishes(search:{keywords:"$keyword"}) {
                name
                recipeNote
                description
                suggestedIngredients{
                    name
                }
            }
        }""")
    query = {
        'query': query_template.substitute(keyword=keyword)}
    r = requests.post(url, json=query, headers=headers)
    data = json.loads(r.text)
    return data


@app.get("/ingredients/{ingredient}")
def get_ingredients(ingredient: str):
    '''
     For getting available ingredients and the substitutes, could be possible 
     if users want to create their own recipe
     '''
    query_template = Template(
        """query ingredients {
            ingredients(searchName:"$ingredient") {
                name
                substitutes{
                    name
                }
            }
        }""")
    query = {
        'query': query_template.substitute(ingredient=ingredient)}
    r = requests.post(url, json=query, headers=headers)
    data = json.loads(r.text)
    return data
