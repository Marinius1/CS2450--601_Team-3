class DummyNode:

    def __init__(self, name: str = "dummy", nodes: list = None):
        self.name = name

        self.nodes = nodes

    def get_nodes(self):

        node_buffer = []

        if self.nodes:
            for i in self.nodes:
                node_buffer.append(i.get_nodes)

        return node_buffer
