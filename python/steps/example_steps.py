#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# steps definition for currency WS

from behave import given, when, then
from models.example import Example


@when('I call the example WS')
def step_impl(context):
    context.requester = Example()
    context.requester.add_params(context.params)
    context.requester.call_get_ws(context.baseUrl)
