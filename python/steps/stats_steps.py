#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from behave import given, when, then
from models.stats import Stats


@when('I call the stats WS')
def step_impl(context):
    context.requeter = Stats()
    context.requeter.add_params(context.params)
    url = context.baseUrl + context.requeter.path
    print("URL",url)
    print("Params",context.requeter.param)
    context.response = requests.get(url, params=context.requeter.param)
    context.requeter.set_response(context.response)


@then('stats result is contains all needed fields')
def step_impl(context):
    context.requeter.validate_response_format()


@then('stats currency is "{currency}"')
def step_impl(context, currency):
    context.requeter.assert_currency(currency)