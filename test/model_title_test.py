#!/usr/bin/env python

import os
from concept_official_copy.model.title import Title
import unittest
import mock

class TestModelTitle(unittest.TestCase):
    def test_init(self):
        t = Title('EXAMPLE')
        assert t.title_number == 'EXAMPLE'

if __name__ == '__main__':
    unittest.main()
