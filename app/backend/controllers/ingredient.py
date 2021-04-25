from ..dependencies import prepare
from string import Template


def get_ingredient(ingredient: str):
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
    data = prepare(query)
    print(data)
    return data
