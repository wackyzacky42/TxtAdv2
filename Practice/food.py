class Food():
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def calories(self):
        return ((self.carbs * 4) + (self.protein * 4) + (self.fat * 9))

class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(self):
        total_calories = 0
        for item in self.ingredients:
            total_calories += item.calories()

        return total_calories

    def __str__(self):
        return self.name

recipes = [Recipe('Ice cream sundae', (Food('Ice cream', 20, 0, 40), Food('Hot fudge', 15, 0, 30), Food('Sprinkles', 5, 0, 0))),
           Recipe('Lentil loaf', (Food('Lentils', 0, 10, 2), Food('Vegetable stock', 5, 0, 0), Food('Mashed potatoes', 20, 0, 2)))]

for item in recipes:
    print('Recipe: {}, Calories: {}'.format(item.name, item.calories()))
