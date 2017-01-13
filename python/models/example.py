#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.requeter import Requester


class Example(Requester):

    def __init__(self):
        super().__init__('weather')

    def validate_response_format(self):
        assert hasattr(self.response, 'text')
