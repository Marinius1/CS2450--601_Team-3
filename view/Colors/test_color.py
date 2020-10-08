import pytest

from color import Color


@pytest.fixture(scope="module")
def base_color():
    return Color()


def test_style_load_file(base_color):
    assert base_color.tree is not None


def test_style_color_config(base_color):
    assert base_color.colors.a0 == '#1d1d1d'
    assert base_color.colors.a9 == '#2830f6'
    assert base_color.colors.background == '#1d1d1d'
    assert base_color.colors.link == '#0e47ca'
    assert base_color.colors.selection == '#a2d3e5'
    assert base_color.colors.bold == '#ffffff'
