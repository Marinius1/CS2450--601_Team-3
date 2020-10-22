import pytest

from ui_node import UINode


@pytest.fixture(scope="function")
def empty_node():
    """returns an empty window with bse size 800 x 600"""
    node = UINode(name="root")

    return node


def test_node_get_children(empty_node):
    c1 = UINode(name="c1")
    c2 = UINode(name="c2")
    c3 = UINode([c1, c2], name="c3")

    empty_node.nodes = [c3]

    children = empty_node.get_children()
    children_keys_iter = children.keys()
    children_keys = []

    for i in children_keys_iter:
        children_keys.append(i)

    assert children_keys[0].name == "root"


def test_node_add_children(empty_node):
    empty_node.add_child(UINode(name="child1"))

    print(empty_node.nodes)

    assert len(empty_node.nodes) == 1
    assert empty_node.nodes[0].name == "child1"


def test_node_composition():
    new_node = UINode([
        UINode([
            UINode(name="top-content-0"),
            UINode(name="top-content-1")
        ],
            name="top-container"
        ),
        UINode([
            UINode(name="bottom-content")
        ],
            name="bottom-container"
        )
    ],
        name="root"
    )

    assert new_node.name == "root"

    assert new_node.nodes[0].name == "top-container"
    assert new_node.nodes[0].nodes[0].name == "top-content-0"
    assert new_node.nodes[0].nodes[1].name == "top-content-1"

    assert new_node.nodes[1].name == "bottom-container"
    assert new_node.nodes[1].nodes[0].name == "bottom-content"
