#!/usr/bin/env python

import os
import re
from concept_official_copy.model.title import Title
import pytest

re_isodatetime = re.compile("^20\d{2}-[0-1]\d-[0-3]\dT[0-2]\d:\d{2}:\d{2}.\d{2,}$")

def test_create_title():
    title = Title('EXAMPLE')

    assert type(title) == Title, ('Title returns a Title, %s, %s' % (type(title), Title))
    assert '<concept_official_copy.model.title.Title object' in '%s' % title

    assert title.title_number == 'EXAMPLE'
    assert re_isodatetime.match(title.accessed) is not None
