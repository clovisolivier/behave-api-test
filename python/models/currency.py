#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.requeter import Requester


class Currency(Requester):

    def __init__(self):
        self.path = 'account/currency'

    def validate_response_format(self):
        assert 'currency' in self.response_body
        currency = self.response_body['currency']
        assert 'symbol' in currency
        assert 'name' in currency
        assert 'iso_a3' in currency

        assert 'levels' in self.response_body
        levels = self.response_body['levels']
        assert 'level0' in levels

        assert 'level0' in self.response_body
        level0 = self.response_body['level0']
        assert isinstance(level0,list)

        assert 'roi_calculation_method' in self.response_body
