from typing import List, Optional
import json
from fastapi import FastAPI, HTTPException, Request, Query
import os
from string import Template
import time
import urllib3
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
url = 'https://api.plantjammer.com/graphql'
http = urllib3.PoolManager()
headers = {
    "Authorization": os.environ.get("API_KEY")}

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Always use pagination if you don't need everything, for performance gains
# See faster-requests pull request for more info on how good pagination is

# With the ids find a dish and return the recipe


@app.get("/")
def read_root_route():
    '''
    Test route
    '''
    return {"Hello": "Adib"}


@app.get("/dishes/{keyword}")
def get_dishes_route(keyword: str):
    '''
    For getting the dishes based on a keyword
    '''
    # we also have serving, estimated time, and suggested ingredients
    data = get_dishes(keyword)
    return data


def get_dishes(keyword: str):
    query_template = Template(
        """query dishes {
            dishes(search:{keywords:"$keyword"}, djangoFilter:{orderBy:"search_score"}) {
                name
                recipeNote
                description
                estimatedPreparationTime
                image{
                    url
                }
                suggestedIngredients{
                    name
                    substitutes{
                        name
                    }
                }
            }
        }""")
    query = {
        'query': query_template.substitute(keyword=keyword)}
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data


@app.get("/ingredients/")
def get_ingredients_route(ingredient: Optional[str] = ""):
    '''
     For getting available ingredients and the substitutes, could be possible
     if users want to create their own recipe
     '''
    print(ingredient)
    data = get_ingredients(ingredient)
    return data


def get_ingredients(ingredient: str):
    query_template = Template(
        """query ingredients {
                ingredients(searchName:"$ingredient") {
                    id
                    name
                    icon{
                        url
                    }
                }
            }""")
    query = {
        'query': query_template.substitute(ingredient=ingredient)}
    print(query)
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    print(data)
    return data


'''
returns a response and missing object which tells you how many of the 
ingredients that you wanted were found with their name and id plus how many 
were not found which are in the missing object
'''


@app.get("/ids/")
def get_ids_route(q: List[str] = Query(None)):
    '''
    To get ids of a list of ingredients
    '''
    data = get_ids(q)
    return data


def get_ids(ingredients: List[str]):
    final_ids = []
    print(ingredients)
    for ingredient in ingredients:
        print(ingredient)
        id = get_ingredients(ingredient)["data"]["ingredients"][0]["id"]
        name = get_ingredients(ingredient)["data"]["ingredients"][0]["name"]
        final_ids.append([id, name])
    data = {"response": final_ids, "missing": len(ingredients)-len(final_ids)}
    print(data)
    return data


@app.get('/recipes/')
def get_recipe_route(q: List[str] = Query(None), id: Optional[List[int]] = Query(None), dish: Optional[str] = Query(None)):
    '''
    To get a recipe based on a string containing all the ingredients
    '''
    print(id)
    print(dish)
    if id:
        print('hi')
        data = get_recipe_ids(dish, id)
    else:
        print('hello')
        data = get_recipe(q)
    return data


def get_recipe(keywords: List[str]):
    ids = [int(i[0]) for i in get_ids(keywords)["response"]]
    print(ids)
    keywords = " ".join(keywords)
    query_template = Template(
        """query getRecipe {
    dishes(search:{keywords:"$keywords"},djangoFilter:{orderBy:"search_score"}){
    searchScore
      name
      estimatedPreparationTime
      description
      mandatoryIngredients{
        name
      }
      image{
          url
      }
      serving {
        name
        amount
      }
      ratio {
        volumes(ingredients:$ids portions: 1) {
          ingredient {
            name
          }
          grams
        }
      }
      blueprint {
        instructions(ingredients:$ids) {
          text
          method
        }
      }
    }
  }""")
    query = {
        'query': query_template.substitute(keywords=keywords, ids=ids)}
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data


def get_recipe_ids(dish: str, ids: List[str]):
    query_template = Template(
        """query getRecipe {
    dishes(search:{keywords:"$dish"},djangoFilter:{orderBy:"search_score"}){
    searchScore
      name
      estimatedPreparationTime
      description
      mandatoryIngredients{
        name
      }
      image{
          url
      }
      serving {
        name
        amount
      }
      ratio {
        volumes(ingredients:$ids portions: 1) {
          ingredient {
            name
          }
          grams
        }
      }
      blueprint {
        instructions(ingredients:$ids) {
          text
          method
        }
      }
    }
  }""")
    query = {
        'query': query_template.substitute(dish=dish, ids=ids)}
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data


@app.get('/substitutes/')
def get_substitutes_route(dish: int = Query(None), sub: List[str] = Query(None)):
    '''
    To get the substitutes based on dish id and some target ingredients
    '''
    data = get_substitutes(dish, sub)
    return data


def get_substitutes(dish: int, sub: List[str]):
    ids = [int(each_id[0]) for each_id in get_ids(sub)['response']]
    # We have to build the query template from scratch since we don't
    # know how many substitutions we want
    query_template_start = 'query getSubstitutes { dishes(id:$dish){ name '
    query_template_middle = ''
    for i in range(len(ids)):
        query_template_middle += 'sub{index}: substituteIngredient(targetIngredient: {id}) {{id name}} '.format(
            index=i, id=ids[i])
    query_template_end = '} }'
    query_template = query_template_start + \
        query_template_middle + query_template_end
    query_template = Template(query_template)
    query = {
        'query': query_template.substitute(dish=dish)}
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data


@app.get('/all_ingredients/{dish}')
def get_all_ingredients_route(dish: str):
    '''
    Get all the ingredients for a dish
    '''
    data = get_all_ingredients(dish)
    return data


def get_all_ingredients(dish: str):
    query_template = Template("""query getRecipe {
    dishes(search:{keywords:"$dish"},djangoFilter:{orderBy:"search_score"}){
    searchScore
      name
    suggestedIngredients{
      name
      id
      substitutes{
        name
      }
    }
     
  }
   } """)
    query = {
        'query': query_template.substitute(dish=dish)}
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data
