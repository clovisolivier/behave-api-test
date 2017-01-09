#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from behave import *
from models.calculator import Calculator


@given('I put "{thing:Number}" in a calculate')
def step_impl(context, thing):
    context.thing = thing


@when('I switch the calculate on')
def step_impl(context):
    weathermanager = Calculator()
    context.response = weathermanager.multiplication(context.thing)


@then('it should transform into "{other_thing:Number}"')
def step_impl(context, other_thing):
    assert context.response == other_thing
