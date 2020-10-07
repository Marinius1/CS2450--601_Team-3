"""
grouping class for a collection of radio widgets. has references to all of
the related radio buttons.
"""

'''
init(name: str, children[]: List<Radio>): void
call super(). populate the child radio elemetns, set 'selected' to false on
each of them.
'''

'''
get_children(mode=0: int): List<mixed>
overrides default get_children method. returns child array and based on the
mode either gives back the widgets themselves, or a dict of <name, value>
pairs.
'''

'''
do(): void
preferred public facing interface for the functionality.
'''