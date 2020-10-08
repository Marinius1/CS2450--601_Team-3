
class Node:

    def __init__(self, name: str = "", nodes=None):

        self.name = name

        self.nodes = nodes
        if nodes is None:
            nodes = []
