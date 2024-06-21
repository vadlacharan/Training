class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def top_view(self):
        my_dict = {}

        queue = [(self.root,0)]
        while queue:
            node,idx = queue.pop(0)

            if idx not in my_dict:
                my_dict[idx] = node.data
            
            if node.left:
                queue.append((node.left,idx-1))
            if node.right:
                queue.append((node.right,idx+1))
        
        for key,value in sorted(my_dict.items()):
            print(value,end=" ")

    def bottom_view(self):
        my_dict = {}
        queue=[(self.root,0)]

        while queue:
            node,idx = queue.pop(0)
            my_dict[idx] = node.data

            if node.left:
                queue.append((node.left,idx-1))
            if node.right:
                queue.append((node.right,idx+1))
            
        for key,value in sorted(my_dict.items()):
            print(value,end=" ")
            
            
            

bst = Tree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(15)
bst.insert(25)

#i8bst.top_view()
bst.bottom_view()
