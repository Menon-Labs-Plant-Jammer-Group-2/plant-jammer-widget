from fastapi import APIRouter, Query
from typing import List, Optional
from ..controllers import ingredient

router = APIRouter(
    prefix="/ingredient",
    tags=["ingredient"],
)


@router.get("/")
def get_ingredient_route(ing: Optional[str] = ""):
    '''
     For getting information on an ingredient
     '''

    print(ingredient)
    data = ingredient.get_ingredient(ing)
    return data
