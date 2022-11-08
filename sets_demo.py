# create a set 
my_foods = {"pancakes", "pizza", "curry", "taco", "gummi bears"}
# print(my_foods)

has_pizza = "pizza" in my_foods
# print(has_pizza)

#add() single item
my_foods.add("frosty")
# print(my_foods)

more_foods = ["burger",  'fries', "pannini"]
my_foods.update(more_foods)
# print(my_foods)

#remove() item
# my_foods.remove("burger")

# pop.() (randomly remove)
# some_foods = my_foods.pop()
# print(my_foods)
# print(some_foods)

# # .clear()
# my_foods.clear()

# Write a function with a set

def food_checker(foods, food_to_find):
    if food_to_find in foods:
        print(f"{food_to_find} is here!")
    else:
        print(f"{food_to_find} is not in this Set")


# food_checker(my_foods, "hummus")

# Math Operations
david_foods = {"pizza", "lentil soup", "mac & cheese", "crab rangoon", "spanish mushroom lasagna"}

megan_foods = {"watermelon", "mac & cheese", "frosted animal cracker", "pad thai", "pizza"}
# union

my_union =david_foods.union(megan_foods)
# print(my_union)

# # intersection
# my_intersection = david_foods.intersection(megan_foods)
# print(my_intersection)

# is disjoint

# is_disjointed = david_foods.isdisjoint(megan_foods)
# print(is_disjointed)

# difference

my_difference = david_foods.difference(megan_foods)
print(my_difference)

