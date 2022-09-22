class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0
    
    def parent_idx(self, idx):
        return idx // 2
    
    def left_child_idx(self, idx):
        return idx * 2
    
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def add(self, element):
        self.count + 1
        self.heap_list.append(element)
        self.heapify_up()
    
    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if ord(parent.value[0]) < ord(child.value[0]):
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)




    