"""
A module containing the :py:class:`Title` class
"""

import datetime

def current_timestring():
    return datetime.datetime.now().isoformat()

class Title(object):
    """
    The primary content object in the Land Registry
    """

    def __init__(self, title_number=None):
        """
        Create a new Title object.

        A ``title_number`` is required to create a new title.
        """
        self.title_number = title_number
        self.created = u''
        self.accessed = current_timestring()
