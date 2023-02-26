from enum import Enum

class RecipeType(Enum):
    STARTER = "starter"
    LUNCH = "lunch"
    DESSERT = "dessert"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

class Recipe:
    def __init__(self, name : str, cooking_lvl : int, cooking_time : int, ingredients : list, recipe_type : str, description : str = ""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        return f"  Name: {self.name}\n\
    - lvl {self.cooking_lvl} - for {self.recipe_type} - time : {self.cooking_time // 60:02d}h {self.cooking_time % 60:02d}m \n\
    - Description: {self.description}\n\
    - Ingredients: {self.ingredients}"

    def __repr__(self):
        return f"Recipe({self.name}, {self.cooking_lvl}, {self.cooking_time}, {self.ingredients}, {self.recipe_type}, {self.description})"