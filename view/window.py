"""
Root window creation logic. this can effectively be a singleton unless we
want to have multiple windows open, though that is not likely. Call once
On application init
"""

'''
Window class: responsible for being the 'root' component of all other widgets,
layout, etc.. has properties like height, width, etc. will most likely handle
resize events as well.
'''

'''
window class init function. Needs to create the window of course, and set up
any window-level logic data pertinent to the view.
'''