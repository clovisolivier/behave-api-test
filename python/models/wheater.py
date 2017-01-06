#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class WeatherManager:


    def __init__(self):
        self.path = 'weather'
        self.param = []
        self.response = ''


    def add_param(self, param):
        self.param.append(param)
