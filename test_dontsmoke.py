"""
Unit tests for dontsmoke
"""

import dontsmoke
from datetime import datetime, timedelta

class TestDontSmoke:

    def test_how_many_days(self):
        stoping_date = datetime(2018, 11, 28)
        assert dontsmoke.how_many_days(stoping_date) >= timedelta(1)
    

    def test_parse_date(self):
        sample_date = "19-03-1989"
        assert datetime(1989, 3, 19) == dontsmoke.parse_date(sample_date)

