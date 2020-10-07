import pytest

from style import Style


@pytest.fixture(scope="module")
def base_style():
    return Style()


def test_style_load_file(base_style):
    assert base_style.tree is not None


def test_style_color_hash(base_style):
    assert base_style.color_hash is not None
