import unittest
from recipe import Recipe
from book import Book
from datetime import datetime

class Test(unittest.TestCase):
    def test_Recipe_00(self):
        recipe = Recipe("test", 1, 10, ["test"], "starter")
        self.assertEqual(recipe.name, "test")
        self.assertEqual(recipe.cooking_lvl, 1)
        self.assertEqual(recipe.cooking_time, 10)
        self.assertEqual(recipe.ingredients, ["test"])
        self.assertEqual(recipe.recipe_type, "starter")
        self.assertEqual(recipe.description, "")

    def test_Recipe_01(self):
        test_input_name = "test"
        test_input_lvl = 1
        test_input_time = 10
        test_input_ingredients = ["test"]
        test_input_type = "starter"
        test_input_description = "test"

        recipe = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)
        
        self.assertEqual(recipe.name, test_input_name)
        self.assertEqual(recipe.cooking_lvl, test_input_lvl)
        self.assertEqual(recipe.cooking_time, test_input_time)
        self.assertEqual(recipe.ingredients, test_input_ingredients)
        self.assertEqual(recipe.recipe_type, test_input_type)
        self.assertEqual(recipe.description, test_input_description)

    def test_Recipe_02(self):
        test_input_name = "test"
        test_input_lvl = 1
        test_input_time = 10
        test_input_ingredients = ["test"]
        test_input_type = "starter"
        test_input_description = "test"

        recipe = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)
        
        self.assertEqual(str(recipe), f"  Name: {test_input_name}\n\
    - lvl {test_input_lvl} - for {test_input_type} - time : {test_input_time // 60:02d}h {test_input_time % 60:02d}m \n\
    - Description: {test_input_description}\n\
    - Ingredients: {test_input_ingredients}")
        
    def test_Recipe_03(self):
        test_input_name = "test"
        test_input_lvl = 1
        test_input_time = 10
        test_input_ingredients = ["test"]
        test_input_type = "starter"
        test_input_description = "test"

        recipe = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)
        
        self.assertEqual(repr(recipe), f"Recipe({test_input_name}, {test_input_lvl}, {test_input_time}, {test_input_ingredients}, {test_input_type}, {test_input_description})")

    def test_Book_00(self):
        test_time = datetime.now()
        book = Book("test", test_time, test_time, [])
        self.assertEqual(book.name, "test")
        self.assertEqual(book.last_update, test_time)
        self.assertEqual(book.creation_date, test_time)
        self.assertEqual(book.recipes_list, [])

    def test_Book_01(self):
        test_time = datetime.now()
        book = Book("test", test_time, test_time, [])
        self.assertEqual(book.get_recipe_by_name("test"), None)
        self.assertEqual(book.get_recipes_by_types("starter"), [])
        self.assertEqual(book.get_recipes_by_types("lunch"), [])
        self.assertEqual(book.get_recipes_by_types("dessert"), [])

    def test_Book_02(self):
        test_time = datetime.now()
        book = Book("test", test_time, test_time, [])

        test_input_name = "test"
        test_input_lvl = 1
        test_input_time = 10
        test_input_ingredients = ["test"]
        test_input_type = "starter"
        test_input_description = "test"

        recipe = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)

        book.add_recipe(recipe)

        self.assertEqual(book.get_recipe_by_name("test"), recipe)
        self.assertEqual(book.get_recipes_by_types("starter"), [recipe])
        self.assertEqual(book.get_recipes_by_types("lunch"), [])
        self.assertEqual(book.get_recipes_by_types("dessert"), [])

    def test_Book_03(self):
        test_time = datetime.now()
        book = Book("test", test_time, test_time, [])

        test_input_name = "test"
        test_input_lvl = 1
        test_input_time = 10
        test_input_ingredients = ["test"]
        test_input_type = "starter"
        test_input_description = "test"

        recipe = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)
        recipe2 = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)
        recipe3 = Recipe(test_input_name, test_input_lvl, test_input_time, test_input_ingredients, test_input_type, test_input_description)

        book.add_recipe(recipe)
        book.add_recipe(recipe2)
        book.add_recipe(recipe3)

        self.assertEqual(book.get_recipe_by_name("test"), recipe)
        self.assertEqual(book.get_recipes_by_types("starter"), [recipe, recipe2, recipe3])
        self.assertEqual(book.get_recipes_by_types("lunch"), [])
        self.assertEqual(book.get_recipes_by_types("dessert"), [])
        


if __name__ == '__main__':
    unittest.main()