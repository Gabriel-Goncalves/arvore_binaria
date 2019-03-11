class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left


class BinaryTree:
    def __init__(self):
        self.root = None

    def empty(self):
        if self.root is None:
            return True
        return False

    def get_root(self):
        return self.root

    def insert(self, key):

        node = Node(key)

        if self.empty():
            self.root = node

        else:

            dad_node = None
            curr_node = self.root

            while True:

                if curr_node is not None:

                    dad_node = curr_node

                    if node.get_key() > curr_node.get_key():
                        curr_node = curr_node.get_right()

                    else:
                        curr_node = curr_node.get_left()

                else:

                    if node.get_key() > dad_node.get_key():
                        dad_node.set_right(node)

                    else:
                        dad_node.set_left(node)
                    break

    def show(self, curr_node):

        if curr_node is not None:
            print(curr_node.get_key(), end=' ')
            self.show(curr_node.get_left())
            self.show(curr_node.get_right())

    def remove(self, key):

        dad_node = None
        curr_node = self.root

        while curr_node is not None:

            if curr_node.get_key() == key:

                # Caso onde o no a ser removido e uma folha
                if curr_node.get_right() is None and curr_node.get_left() is None:

                    # Verifica se e a raiz
                    if dad_node is None:
                        self.root = None

                    else:
                        # Verifica se é o no a direita ou a esquerda do pai
                        if dad_node.get_left() is curr_node:
                            dad_node.set_left(None)
                        elif dad_node.get_right() is curr_node:   # erro 1
                            dad_node.set_right(None)

                # Caso 2 onde o no possui apenas 1 filho
                elif (curr_node.get_left() is not None and curr_node.get_right() is None) \
                        or (curr_node.get_left() is None and curr_node.get_right() is not None):

                    # verifica se o no a ser removido e a raiz
                    if dad_node is None:

                        # se o no a ser removido e o da esquerda
                        if curr_node.get_left() is not None:
                            self.root = curr_node.get_left()
                        else:
                            self.root = curr_node.get_right()

                    else:

                        # Verifica se o no a ser removido é o da esquerda
                        if curr_node.get_left() is not None:
                            # Verifica se o pai aponta para a esquerda
                            if dad_node.get_left()and dad_node.get_left() \
                                    is curr_node:
                                dad_node.set_left(curr_node.get_left())
                            else:
                                dad_node.set_right(curr_node.get_left())

                        else:
                            if dad_node.get_left() is curr_node:  # possivel erro 144

                                dad_node.set_left(curr_node.get_right())
                            else:
                                dad_node.set_right(curr_node.get_right())

                # caso 3: o nó a ser removido possui dois filhos
                # pega-se o menor elemento da sub-arvore à direita
                elif (curr_node.get_left() is not None) and (curr_node.get_right() is not None):
                    print('gabriel')
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.get_right()
                    next_smaller = curr_node.get_right().get_left()

                    while next_smaller is not None:
                        print('segundo')
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.get_left()

                    # verifica se é a raiz
                    if dad_node is None:

                        # caso o filho a direita da raiz seja o menor
                        if self.root.get_right().get_key() is smaller_node.get_key():
                            smaller_node.set_left(self.root.get_left())
                        else:
                            if dad_smaller_node is not None \
                                    and dad_smaller_node.get_left() is smaller_node:
                                dad_smaller_node.set_left(None)
                            else:
                                dad_smaller_node.set_right(None)

                            # Faz com que os filhos do no a ser removido sejam os filhos do smaller node
                            smaller_node.set_left(curr_node.get_left())
                            smaller_node.set_right(curr_node.get_right())

                        # Como ainda estamos tratando da raiz fazemos com que a raiz seja o smaller node
                        self.root = smaller_node

                    else:

                        '''
                        verifica se curr_node é filho à esquerda ou à direita
                        para setar o smaller_node como filho do pai do curr_node (dad_node)
                        '''
                        if dad_node.get_left() and dad_node.get_left is curr_node:

                            dad_node.set_left(smaller_node)
                        else:
                            dad_node.set_left(smaller_node)

                        '''
                        verifica se o smaller_node é filho à esquerda ou à direita
                        para setar para None o smaller_node
                        '''

                        if dad_smaller_node.get_left() and \
                                dad_smaller_node.get_left() is smaller_node:
                            dad_smaller_node.set_left(None)
                        else:
                            dad_smaller_node.set_right(None)

                        smaller_node.set_left(curr_node.get_left())
                        smaller_node.set_right(curr_node.get_right())
                break

            dad_node = curr_node

            if key < curr_node.get_key():
                curr_node = curr_node.get_left()
            else:
                curr_node = curr_node.get_right()


t = BinaryTree()

t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)
t.show(t.get_root())
print()
t.remove(8)
t.show(t.get_root())
