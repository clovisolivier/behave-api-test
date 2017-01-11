#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Common steps definition

from behave import *


@given('I clean params in context')
def step_impl(context):
    context.params = {}
    context.post_params = {}


@given(u'I want to set "{data}" in param "{param:Str}"')
def step_impl(context, data, param):
    context.params[param] = data


@given(u'I set "{data}" value in POST param "{param:Str}"')
def step_impl(context, data, param):
    context.post_params[param] = data


@then('status code should be {status_code:Number}')
def step_impl(context, status_code):
    assert hasattr(context,'requester')
    context.requester.assert_status_code(status_code)


@then('error message should be on "{attribute:Str}"')
def step_impl(context, attribute):
    assert hasattr(context, 'requester')
    context.requester.assert_error_attribute(attribute)
