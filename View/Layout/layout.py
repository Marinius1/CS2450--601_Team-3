"""
root layout widget. holds all of the information needed for subclasses to
function properly irrespective of specific implementation details. also
handles things like resize and visibility toggling.
"""

'''
init(name: str, children[]: List<varied>): void
builds out layout and arguably of more importance, sets up resize event
handlers. sets visibility to False initially.
'''

'''
get_children(): List<varied>
traverse all child nodes, building a list using a Depth-First Traversal (DFT).
return this list. will liekly work in a recursive manner.
'''

'''
resize(): void
listen for tkinter resize event and reset the size of all child widgets as
needed. will only execute if visible == True.
'''

'''
toggle(): void
toggle the visibility value, and either hide or show relevant widgets based
on the current visible state. 
'''