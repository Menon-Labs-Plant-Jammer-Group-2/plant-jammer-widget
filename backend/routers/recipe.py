from fastapi import APIRouter, Query
from typing import List, Optional
from ..controllers import recipe

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
)


@router.get('/',)
def get_recipe_route(keywords: List[str] = Query(None), id: Optional[List[int]] = Query(None), dish: Optional[str] = Query(None), chosen: Optional[List[str]] = Query(None)):
    '''
    To get a recipe based on a string containing all the ingredients
    '''
    if id:
        data = recipe.get_recipe_ids(dish, id, chosen)
    else:
        data = recipe.get_recipe(keywords)
    return data
