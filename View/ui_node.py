"""
self-contained node for the ui system will be used to build a small tree
data structure of ui nodes
"""
import uuid as UUID


class UINode:
    """
    base class for all ui nodes, holds children, also
    """

    def __init__(self, nodes=None, name: str = ""):

        if nodes is None:
            nodes = []
        self.nodes = nodes

        self.name = name
        self.uuid = UUID.uuid4()

    def __hash__(self):
        return hash((self.name, self.uuid))

    def __eq__(self, other):
        return (self.name, self.uuid) == (other.name, other.uuid)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def get_children(self):
        children = {}

        if len(self.nodes) == 0:
            pass
        else:
            children[self] = {}
            for i in self.nodes:
                children[self][i] = i.get_children()

        return children

    def add_child(self, child=None):
        if child is not None:
            self.nodes.append(child)
