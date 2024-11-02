dict_food = {"apple" : 130,"banana" : 110,"Sweet Cherries": 100,"pear":100,"Kiwifruit":90,"Avocado":50}
fruit_asked = input("Item: ")
for key in dict_food:
    if key == fruit_asked:
        print("Calories", dict_food[key])