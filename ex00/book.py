from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name : str, last_update : datetime, creation_date : datetime, recipes_list : dict):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name : str):
        for recipe in self.recipes_list:
            if recipe.name == name:
                return recipe
        return None
    
    def get_recipes_by_types(self, recipe_type : str):
        return [recipe for recipe in self.recipes_list if recipe.recipe_type == recipe_type]
    
    def add_recipe(self, recipe : Recipe):
        if isinstance(recipe, Recipe) == False:
            raise TypeError("recipe must be a Recipe")
        self.recipes_list.append(recipe)
        self.last_update = datetime.now()