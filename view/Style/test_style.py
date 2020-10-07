import pytest

from style import Style


@pytest.fixture(scope="module")
def base_style():
    return Style()


def test_style_load_file(base_style):
    assert base_style.tree is not None


def test_style_color_confg(base_style):
    assert base_style.colors.a0 == '#1d1d1d'
    assert base_style.colors.a9 == '#2830f6'
    assert base_style.colors.background == '#1d1d1d'
    assert base_style.colors.link == '#0e47ca'
    assert base_style.colors.selection == '#a2d3e5'
    assert base_style.colors.bold == '#ffffff'
