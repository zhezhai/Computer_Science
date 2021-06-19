class BinaryTree:
    def __init__(self, root):
        self.key = root 
        self.leftChild = None
        self.rightChild = None

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self, val):
        self.key = val 
    
    def getRootVal(self):
        return self.key
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftchild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t 
    

