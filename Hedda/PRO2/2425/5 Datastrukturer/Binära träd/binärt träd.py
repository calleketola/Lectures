class Node():

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

class Binary_tree():

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
        out = self._io_print(self.root)
        out += "\n"
        out += self._pre_print(self.root)
        out += "\n"
        out += self._post_print(self.root)
        return out

    def _io_print(self, node):
        if node is None:
            return ""
        out = ""
        out += self._io_print(node.left)
        out += str(node.value) + ","
        out += self._io_print(node.right)+", "
        return out[:-2]

    def _pre_print(self, node):
        out = ''
        out += str(node.value)+", "
        if node.left:
            out += self._pre_print(node.left)+", "
        if node.right:
            out += self._pre_print(node.right)+", "
        return out[:-2]

    def _post_print(self, node):
        out = ''
        if node.left:
            out += self._post_print(node.left)+", "
        if node.right:
            out += self._post_print(node.right)+", "
        out += str(node.value)+", "
        return out[:-2]
            
                
