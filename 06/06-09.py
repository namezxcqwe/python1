m = int(input())
ice = set()
n = int(input())
recipes = []
for i in range(n):
    recipes_name = input()
    num_ing = int(input())
    ing = set()
    if ing.intersection(ice):
        recipes.append(recipes_name)
for recipe in recipes:
    print(recipe)