class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():

    def __init__(self):
        self.root = None

    def push(self, value):
        # Om det inte finns någon rot,
        # skapa en rot
        if self.root == None:
            self.root = Node(value)
        else:
            # Vi börjar på roten
            current = self.root
            # En variabel för att hålla reda på att
            # vi letar
            searching = True
            # Sök efter rätt position
            while searching:
                # Kontrollera om vi ska till höger
                # eller om vi ska till vänster
                if value >= current.value:
                    # Kontrollera om vi har ett
                    # barn till höger
                    if current.right == None:
                        # Har vi inget barn till
                        # höger stoppa in värdet
                        # och sluta leta
                        current.right = Node(value)
                        searching = False
                    else:
                        # Annars så uppdaterar vi
                        # current till nästa nod
                        current = current.right
                else:
                    # Kontrollera om vi har ett
                    # barn till vänster
                    if current.left == None:
                        # Har vi inget barn till
                        # vänster stoppa in värdet
                        # och sluta leta
                        current.left = Node(value)
                        searching = False
                    else:
                        # Annars så uppdaterar vi
                        # current till nästa nod
                        current = current.left
                        



        
        
