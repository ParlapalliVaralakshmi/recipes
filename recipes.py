class RecipeSearchApp:
    def __init__(self):
        self.recipes = {
            "Pasta Carbonara": ["pasta", "eggs", "bacon", "parmesan"],
            "Chicken Stir-Fry": ["chicken", "vegetables", "soy sauce"],
            # Add more recipes
        }

    def search_recipes(self, user_ingredients):
        user_ingredients = set(user_ingredients)
        matched_recipes = []

        for recipe, ingredients in self.recipes.items():
            if user_ingredients.issubset(set(ingredients)):
                matched_recipes.append(recipe)

        return matched_recipes

    def run(self):
        print("Welcome to the Recipe Search App!")

        while True:
            user_input = input("Enter the ingredients you have (comma-separated), or type 'exit' to quit: ")

            if user_input.lower() == 'exit':
                break

            user_ingredients = [ingredient.strip() for ingredient in user_input.lower().split(',')]
            matched_recipes = self.search_recipes(user_ingredients)

            if matched_recipes:
                print("\nMatching Recipes:")
                for recipe in matched_recipes:
                    print(recipe)
            else:
                print("\nNo matching recipes found.")

        print("Goodbye!")

if __name__ == "__main__":
    app = RecipeSearchApp()
    app.run()
