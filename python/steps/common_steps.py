#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Common steps definition

from behave import *


@given('I clean params in context')
def step_impl(context):
    context.params = {}
    context.post_params = {}


@given('I want to call WS with account_id {account_id}')
def step_impl(context, account_id):
    context.params['account_id'] = account_id


@given(u'I want data between "{date_from}" and "{date_to}"')
def step_impl(context, date_from, date_to):
    context.params['date_from'] = date_from
    context.params['date_to'] = date_to


@given(u'I want data after "{date_from}"')
def step_impl(context, date_from):
    context.params['date_from'] = date_from


@given(u'I want data before "{date_to}"')
def step_impl(context, date_to):
    context.params['date_to'] = date_to


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
