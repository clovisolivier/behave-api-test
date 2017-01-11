#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# steps definition for currency WS

from behave import given, when, then
from models.example import Currency


@when('I call the currency WS')
def step_impl(context):
    context.requester = Currency()
    context.requester.add_body_request_param(context.post_params)
    context.requester.call_post_ws(context.baseUrl)
