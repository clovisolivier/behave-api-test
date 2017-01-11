#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from behave import given, when, then
from models.has_stats import HasStats


@when('I call the has_stat WS')
def step_impl(context):
    context.requester = HasStats()
    context.requester.add_params(context.params)
    context.requester.call_get_ws(context.baseUrl)


@then('this account has no stat')
def step_impl(context):
    context.requester.assert_no_has_stat()


@then('this account has stat')
def step_impl(context):
    context.requester.assert_has_stat()
