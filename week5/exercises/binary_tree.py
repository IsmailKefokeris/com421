
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
    
    def insertNode(self, value):
        if (value < self.value):
            while self.left is not None:
                self.left = self.left
                
            self.left = TreeNode(value)
        elif (value > self.value):
            pass

        


class BinaryTree():

    def __init__(self,Rvalue):
        self.root = TreeNode(Rvalue)

    def insert(self,value):

        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insertNode(value)

    def printTree(self):
        pass


binary = BinaryTree(100)

binary.insert(50)