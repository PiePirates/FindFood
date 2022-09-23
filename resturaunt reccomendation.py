from Tree import *
from restaurantData import *
#building the structure of the tree

def heap_sort(lst):
    sort = []
    maxheap = MaxHeap()
    for element in lst:
        maxheap.add(element)
    while maxheap.count > 0:
        max_value = maxheap.retrieve_max()
        
        sort.insert(0, max_value)
    return sort

list_2d = []
for type in types:
    list_2d.append(Tree(type))

for node in list_2d:
    for restaurant in restaurant_data:
        if restaurant[0] is node.value:
            node.add_child(restaurant)

list_2d = heap_sort(list_2d)

root = Tree(None)
for type in types:
    root.children.append(Tree(type))

for node in root.children:
    for restaurant in restaurant_data:
        if restaurant[0] is node.value:
            node.add_child(restaurant)

#function to get user input
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

#function to search for restaurants based on the type you want

def search(lst, target = None):
    if target is None:
        target = get_user_input()
    middle_idx = len(lst) // 2
    if ord(lst[middle_idx].value[0]) > ord(target[0]):
        for i in range(len(lst)):
            if lst[i].value == target:
                return lst[i].children
    elif ord(lst[middle_idx].value[0]) < ord(target[0]):
        for i in range(len(lst)):
            if lst[-i].value == target:
                return lst[-i].children
    elif target == lst[middle_idx].value:
        return lst[middle_idx].children
    else:
        for i in range(len(lst)):
            if lst[i].value == target:
                return lst[i].children
    return None

def find_restaurants():

    for restaurant in search(list_2d):
        print(f"\nName: {restaurant[1]}\nPrice: {restaurant[2]}/5\nRatings: {restaurant[3]}/5\nLocation: {restaurant[4]}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_input = input("Would you like to search for more restaurants? \"y\" for yes and any key for no.\n")
    if user_input == "y":
        find_restaurants()
    else:
        print("Thanks for using FindFood!")



find_restaurants()









