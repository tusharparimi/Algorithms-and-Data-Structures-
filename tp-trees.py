class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def pre_search(self,start,find_val):
        if start:
            if(start.value==find_val): return True
            else:
                return self.pre_search(start.left,find_val) or self.pre_search(start.right,find_val)
        return False
    def pre_print(self,start):
        if start:
            print(start.value,end=",")
            self.pre_print(start.left)
            self.pre_print(start.right)

    
    def in_print(self,start):
        if start:
            self.in_print(start.left)
            print(start.value,end=",")
            self.in_print(start.right)

    def post_print(self,start):
        if start:
            self.post_print(start.left)
            self.post_print(start.right)
            print(start.value,end=",")


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print (tree.pre_search(tree.root,4))
# Should be False
print (tree.pre_search(tree.root,6))
# Test print_tree
# Should be 1-2-4-5-3
tree.pre_print(tree.root)
print("\n")


tree.in_print(tree.root)
print("\n")
tree.post_print(tree.root)