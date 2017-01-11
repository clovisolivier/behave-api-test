#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from behave import given, when, then
from models.stats import Stats


@when('I call the stats WS')
def step_impl(context):
    context.requester = Stats()
    context.requester.add_params(context.params)
    context.requester.call_get_ws(context.baseUrl)


@then('stats result is contains all needed fields')
def step_impl(context):
    context.requester.validate_response_format()


@then('stats currency is "{currency}"')
def step_impl(context, currency):
    context.requester.assert_currency(currency)