"""
test_window.py
"""

import pytest
import dummy

import tkinter as tk
from window import Window


@pytest.fixture(scope="module")
def empty_window():
    """returns an empty window with bse size 800 x 600"""
    app = Window(tk.Tk())

    return app


def test_window_init(empty_window):
    """validate that the Window object is able to init"""
    assert isinstance(empty_window, Window)
    assert isinstance(empty_window.master, tk.Tk)


def test_window_dimensions(empty_window):
    """assert initial window size is correct"""
    assert empty_window.width == 800
    assert empty_window.height == 600


def test_window_set_size(empty_window):
    """test window resize method"""
    new_size = [600, 400]

    empty_window.size = new_size
    assert new_size == empty_window.size


def test_window_mainloop(empty_window):
    """simple test to ensure mainloop works"""
    # comment this line out if you want to not quit immediately
    # empty_window.after(100, empty_window.master.destroy)
    empty_window.mainloop()
