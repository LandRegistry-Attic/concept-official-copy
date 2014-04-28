#!/usr/bin/env python

import os
from concept_official_copy import service
import unittest
import mock

class TestOfficialCopyService(unittest.TestCase):
    def setUp(self):
        service.app.config['TESTING'] = True
        self.app = service.app.test_client()

    def test_root(self):
        rv = self.app.get('/')
        assert 'Land Registry' in rv.data

if __name__ == '__main__':
    unittest.main()
