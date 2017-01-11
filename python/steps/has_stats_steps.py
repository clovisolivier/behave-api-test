#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from behave import given, when, then
from models.has_stats import HasStats


@when('I call the stats API has_stat')
def step_impl(context):
    context.requeter = HasStats()
    context.requeter.add_params(context.params)
    url = context.baseUrl + context.requeter.path
    print("URL", url)
    print("Params", context.requeter.param)
    context.response = requests.get(url, params= context.requeter.param)
    context.requeter.set_response(context.response)


@then('this account has no stat')
def step_impl(context):
    context.requeter.assert_no_has_stat()


@then('this account has stat')
def step_impl(context):
    context.requeter.assert_has_stat()
