from fastapi import APIRouter, Query
from typing import List, Optional
from ..controllers import ids
router = APIRouter(
    prefix="/ids",
    tags=["ids"],

)


@router.get("/")
def get_ids_route(q: List[str] = Query(None)):
    '''
    To get ids of a list of ingredients
    '''
    data = ids.get_ids(q)
    return data
