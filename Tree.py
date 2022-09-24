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
    
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count
    
    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()
    
    def retrieve_max(self):
        if self.count == 0:
            return None
        max_value = self.heap_list[1]
        self.heap_list[1] = Tree(".")
        self.count -= 1
        self.heap_list.pop(1)
        self.heapify_down()
        return max_value
  
    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child.value[0] != right_child.value[0]:
                if ord(left_child.value[0]) > ord(right_child.value[0]):
                    return self.left_child_idx(idx)
                else:
                    return self.right_child_idx(idx)
            else:
                if ord(left_child.value[1]) > ord(right_child.value[1]):
                    return self.left_child_idx(idx)
                else:
                    return self.right_child_idx(idx)
    
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            if ord(parent.value[0]) < ord(child.value[0]):
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx
    
    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if ord(parent.value[0]) < ord(child.value[0]):
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)




    