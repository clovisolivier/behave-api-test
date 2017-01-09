#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class WeatherManager:


    def __init__(self):
        self.path = 'weather'
        self.param = ''
        self.response = ''


    def add_param(self, param):
        self.param = param
        print( 'add param : ' + param)


    def multiplication(self,param):
        return param * param