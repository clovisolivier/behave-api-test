#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from behave import *

from models.wheater import WeatherManager

baseUrl = 'http://openweathermap.org/data/2.5/'


@given('we call the weather API for {localisation:Str}')
def step_impl(context, localisation):
    weathermanager = WeatherManager()
    weathermanager.add_param('London')
    print(weathermanager.param)
    url = baseUrl + 'weather?q=' + localisation
    data = '';
    context.response = requests.get(url, data)


@then('status code should be {status_code:Number}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code
