from typing import Optional
import json
from fastapi import FastAPI, HTTPException, Request
import os
from string import Template
import time
import urllib3


app = FastAPI()
url = 'https://api.plantjammer.com/graphql'
http = urllib3.PoolManager()
headers = {
    "Authorization": os.environ.get("API_KEY")}

# Always use pagination if you don't need everything, for performance gains
# See faster-requests pull request for more info on how good pagination is


@app.get("/")
def read_root():
    return {"Hello": "Adib"}


@app.get("/recipes/{keyword}")
def get_recipes(keyword: str):
    '''
    For getting the recipes based on a keyword
    '''
    start_time = time.time()

    # we also have serving, estimated time, and suggested ingredients
    query_template = Template(
        """query dishes {
            dishes(search:{keywords:"$keyword"}, pagination:{limitTo:5}) {
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
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
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
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data
