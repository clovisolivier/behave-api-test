#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.requeter import Requester


class HasStats(Requester):

    ATTRIBUTE_HAS_STATS = 'has_stats'

    def __init__(self):
        self.path = 'account/has_stats'

    def assert_has_stat(self):
        assert HasStats.ATTRIBUTE_HAS_STATS in self.response_body
        assert self.response_body[HasStats.ATTRIBUTE_HAS_STATS] is True

    def assert_no_has_stat(self):
        assert HasStats.ATTRIBUTE_HAS_STATS in self.response_body
        assert self.response_body[HasStats.ATTRIBUTE_HAS_STATS] is False
