"""
A module containing the :py:class:`Title` class
"""

import datetime
import jsonpickle

def current_timestring():
    return datetime.datetime.now().isoformat()

class Title(object):
    """
    The primary content object in the Land Registry
    """

    def __init__(self, title_number=None, data=None):
        if data:
            self.__dict__ = data
        if title_number:
            self.title_number = title_number
        self.accessed = current_timestring()

    def as_json(self):
        return jsonpickle.encode(self)
