#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from behave import given, when, then
from models.currency import Currency


@when('I call the currency WS')
def step_impl(context):
    context.requeter = Currency()
    context.requeter.add_body_request_param(context.post_params)
    url = context.baseUrl + context.requeter.path
    context.response = requests.post(url, data=context.requeter.body_param)
    print("URL", context.response.url)
    print("Body params", context.requeter.body_param)
    context.requeter.set_response(context.response)



