"""
button input widget. allows the user to execute a defined action on
click. is configurable to either show text, show an image, or both. also
manages animation states.
"""

'''
init(name: str, text: str, image_path: str, children=[]: List<mixed>, 
type: int): void
init method. calls super() to properly initialize all class data members.
also calls appropriate class methods as needed.
'''

'''
@abstract method implementation
do(): void
class level implementation of this method. will emit an appropriate
signal to the controller.
'''

'''
click(): void
method bound to the button click event. executes the do() method as well as any
additional logic that may be needed.
'''

'''
set_text(text: str): void
overrides the current text data member with a new value.
'''

'''
set_image_path(image_path: str): void
override the current image path with a new value. force image reload if needed.
'''

'''
set_type(type: int): void
set the type of the button widget. (0: text, 1: image, 2: both) and rebuild.
'''
