from fastapi import APIRouter
from ..controllers import all_ingredients

router = APIRouter(
    prefix="/all_ingredients",
    tags=["all_ingredients"],
)


@router.get('/{dish}')
def get_all_ingredients_route(dish: str):
    '''
    Get all the ingredients for a dish
    '''
    data = all_ingredients.get_all_ingredients(dish)
    return data
