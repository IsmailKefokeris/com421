
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
    
    def insert(self, current, root):

        if (current < root.value and root.left == None):
            root.left = TreeNode(current)
        elif (current > root.value and root.right == None):
            root.right = TreeNode(current)
        elif (current < root.value and root.left is not None):
            root = root.left
            TreeNode.insert(self, current, root)
        elif (current > root.value and root.right is not None):
            root = root.right
            TreeNode.insert(self, current, root)   

    def printT(self, value):
          
        while value.left is not None:
            value = value.left
            if value.left is None:
                print(value.value)
            TreeNode.printT(self, value)
            

        while value.right is not None:
            value = value.right
            if value.right is None:
                print(value.value)
            TreeNode.printT(self, value)

        return value.value


class BinaryTree(): 

    def __init__(self,Rvalue):
        self.root = TreeNode(Rvalue)

    def insert(self,value):

        root = self.root
        TreeNode.insert(self, value, root)

    def printTree(self, starting_node):

        if starting_node.left is not None:
            self.printTree(starting_node.left)
        print(starting_node.value)
        if starting_node.right is not None:
            self.printTree(starting_node.right)



binary = BinaryTree(100)

binary.insert(50)
binary.insert(45)
binary.insert(60)
binary.insert(49)
binary.printTree(binary.root)