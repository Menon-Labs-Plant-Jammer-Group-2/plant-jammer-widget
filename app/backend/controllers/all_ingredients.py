
from string import Template
from ..dependencies import prepare


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
    data = prepare(query)
    return data
