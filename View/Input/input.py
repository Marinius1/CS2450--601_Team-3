"""
base input widget class. responsible for defining abstract methods as well as
initializing any common data types between the various types of derived
input widgets.
"""

'''
init(name: str, children=[]: List<mixed>, style=default: Colors): void
will likely be called using the super() method. Will also 
initialize relevant data fields.
'''

'''
@abstractmethod do(): void function. has no definition in this class, 
though subclasses will have their own definition.
'''

'''
@abstractmethod
hover(): void
set up hover event triggers and base functionality, which will include setting
up the tooltip functionality. this can be overridden and care must be taken to
re-implement the tooltip logic if overridden.
'''

'''
tooltip(message: str, delay: float): void
set up the tooltip. also sets up proper time delay for hover events so the 
user's screen is not spammed endlessly with hover events. 
'''

'''
get_children(): List<mixed>
this method traverses all of the child nodes of this ui element and returns 
a list in Breadth First order.
'''

'''
set_style(style: Colors): void
override the default style previously set.
'''