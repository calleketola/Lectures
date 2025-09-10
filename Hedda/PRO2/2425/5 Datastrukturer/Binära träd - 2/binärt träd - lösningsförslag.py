class Node():

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

class BinaryTree():

    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            check = True
            while check:
                if value >= current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        check = False
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        check = False

    def __str__(self):
        
        if self.root is None:
            return ""
        # In order print
        out = self.io_print(self.root)
        out += "\n"
        out += self.pre_print(self.root)
        out += "\n"
        out += self.post_print(self.root)
        return out

    def io_print(self, node):
        if node is None:
            return ""
        out = ""
        out += self.io_print(node.left)
        out += str(node.value) + ", "
        out += self.io_print(node.right)+", "
        return out[:-2]

    def pre_print(self, node):
        out = ''
        out += str(node.value)+", "
        if node.left:
            out += self.pre_print(node.left)+", "
        if node.right:
            out += self.pre_print(node.right)+", "
        return out[:-2]

    def post_print(self, node):
        out = ''
        if node.left:
            out += self.post_print(node.left)+", "
        if node.right:
            out += self.post_print(node.right)+", "
        out += str(node.value)+", "
        return out[:-2]
            
                
tree = BinaryTree()

tal = [5,13,8,15,2,1,9,10,3,11,14,4,6,7,12]

for x in tal:
    tree.push(x)

print(tree)
