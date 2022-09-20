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

for node in root.children:
    print(node.children)
#begining of user input







