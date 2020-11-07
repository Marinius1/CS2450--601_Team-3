import pytest
from glob import glob

from color import Color


@pytest.fixture(scope="module")
def base_color():
    return Color()


def test_style_load_file(base_color):
    """ensure xml tree is loaded"""
    assert base_color.tree is not None


def test_color_parser(base_color):
    """test the parser against all xml .itermcolor files"""
    schemes_path = base_color.scheme_path[:42] + "*.itermcolors"

    schemes = glob(schemes_path)

    for i in schemes:
        base_color.scheme_path = i

        config = base_color.load_color_config()
        assert config is not None


def test_style_color_config(base_color):
    """spot check color hex values"""
    assert base_color.colors.a0 == '#1d1d1d'
    assert base_color.colors.a9 == '#2830f6'
    assert base_color.colors.background == '#1d1d1d'
    assert base_color.colors.link == '#0e47ca'
    assert base_color.colors.selection == '#a2d3e5'
    assert base_color.colors.bold == '#ffffff'
