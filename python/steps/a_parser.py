#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Need to be

from behave import *
import parse


# -- TYPE CONVERTER: For a simple, positive integer number.
@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


# -- REGISTER TYPE-CONVERTER: With behave
register_type(Number=parse_number)
register_type(Str=str)
