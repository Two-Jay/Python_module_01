from enum import Enum

class Gaurd(Enum):
    STRICT = 0
    INHARIANT = 1
    
    @staticmethod
    def validate(value, expected_type, validation_level = STRICT):
        if validation_level == validation_level.INHARIANT:
            if not isinstance(value, expected_type):
                raise TypeError(f"Expected {expected_type}, got {type(value)}")
        elif validation_level == validation_level.STRICT:
            if type(value) != expected_type:
                raise TypeError(f"Expected {expected_type}, got {type(value)}")
        return value

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
        self.name = Gaurd.validate(name, str)
        self.cooking_lvl = Gaurd.validate(cooking_lvl, int)
        self.cooking_time = Gaurd.validate(cooking_time, int)
        self.ingredients = Gaurd.validate(ingredients, list)
        self.recipe_type = Gaurd.validate(recipe_type, str)
        self.description = Gaurd.validate(description, str)

    def __str__(self):
        return f"  Name: {self.name}\n\
    - lvl {self.cooking_lvl} - for {self.recipe_type} - time : {self.cooking_time // 60:02d}h {self.cooking_time % 60:02d}m \n\
    - Description: {self.description}\n\
    - Ingredients: {self.ingredients}"

    def __repr__(self):
        return f"Recipe({self.name}, {self.cooking_lvl}, {self.cooking_time}, {self.ingredients}, {self.recipe_type}, {self.description})"