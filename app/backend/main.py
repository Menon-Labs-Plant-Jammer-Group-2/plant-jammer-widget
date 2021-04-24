from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from .routers import recipe, all_ingredients, ids, ingredient

# Always use pagination if you don't need everything, for performance gains
# See faster-requests pull request for more info on how good pagination is

app = FastAPI()


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

app.include_router(recipe.router)
app.include_router(all_ingredients.router)
app.include_router(ids.router)
app.include_router(ingredient.router)


@app.get("/")
def read_root_route():
    '''
    Test route
    '''
    return {"Hello": "Adib"}
