#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.requeter import Requester


class Example(Requester):

    def __init__(self):
        self.path = 'example'

    def validate_response_format(self):
        assert hasattr(self.response, 'text')
