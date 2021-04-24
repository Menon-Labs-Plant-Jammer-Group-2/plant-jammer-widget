from . import ingredient
from typing import List


def get_ids(ingredients: List[str]):
    final_ids = []
    for ing in ingredients:
        print(ing)
        id = ingredient.get_ingredient(
            ing)["data"]["ingredients"][0]["id"]
        name = ingredient.get_ingredient(
            ing)["data"]["ingredients"][0]["name"]
        final_ids.append([id, name])
    data = {"response": final_ids, "missing": len(ingredients)-len(final_ids)}
    print(data)
    return data
