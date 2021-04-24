from string import Template
from typing import List
from ..dependencies import prepare
from ..controllers import ids


def get_recipe(keywords: List[str]):
    list_ids = [int(i[0]) for i in ids.get_ids(keywords)["response"]]
    print(list_ids)
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
        'query': query_template.substitute(keywords=keywords, ids=list_ids)}
    data = prepare(query)
    return data


def get_recipe_ids(dish: str, q_id: List[int], chosen: List[str]):
    chosen_ids = [int(each_id[0])
                  for each_id in ids.get_ids(chosen)['response']]

    q_id += chosen_ids
    print(q_id)
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
        'query': query_template.substitute(dish=dish, ids=q_id)}
    data = prepare(query)
    return data
