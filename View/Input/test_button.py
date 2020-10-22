"""
test_button.py
"""

import pytest

import tkinter as tk
from button import Button


@pytest.fixture(scope="module")
def base_button():
    """returns an empty window with bse size 800 x 600"""
    btn = Button()

    return btn
