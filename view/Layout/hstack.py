"""
the 'row' class. creates a view that arranges children horizontally within
it's bounds. can auto wrap or truncate if needed. scrolling is also an
option.
"""

'''
init(name: str, children[]: List<varies>): void
calls super(). needs to populate the horizontal view. also needs to bind either 
truncate or wrap data when the contents of the horizontal view exceed the
bounds.
'''