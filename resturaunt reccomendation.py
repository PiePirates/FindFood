from webbrowser import get
from Tree import Tree
from restaurantData import *

#building the structure of the tree
root = Tree(None)
for type in types:
    root.children.append(Tree(type))

for node in root.children:
    for restaurant in restaurant_data:
        if restaurant[0] is node.value:
            node.add_child(restaurant)

#for node in root.children:
    #print(node.children)

#begining of user input
def get_user_input(user_input = None):
    if user_input is None:
        user_input = input("What type of food would you like to eat today?\n")
        if user_input in types:
            return user_input
        elif user_input[0] in [type[0] for type in types]:
            return get_user_input(user_input)
        else:
            print("Sorry we don't have any restaurants that serve that type of food.\nPlease try searching again.\n")
            return get_user_input()
    else:
        types_for_input = [type for type in types if type[0] == user_input[0]]
        types_for_input_string = ", ".join(types_for_input)
        user_input_2 = input(f"What you entered is close to these types of food: {types_for_input_string}.\nPlease enter one of the following or type \"return\" to search again.\n")
        if user_input_2 in types_for_input:
            return user_input_2
        elif user_input_2 == "return":
            return get_user_input()
        else:
            return get_user_input(user_input)

            
        

        

print(get_user_input())







