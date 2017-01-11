#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


# Tool to managed http requests
class Requester:

    def __init__(self):
        # Get params
        self.param = {}
        # Post Params
        self.body_param = {}
        # Http response
        self.response = ''
        # Response Body
        self.response_body = {}

    def add_params(self, params_list):
        self.param = params_list

    def add_body_request_param(self, params_list):
        self.body_param = params_list

    def set_response(self, response):
        self.response = response
        assert hasattr(response, 'text')
        self.response_body = json.loads(response.text)

    def assert_status_code(self, status_code):
        assert hasattr(self.response, 'status_code')
        assert self.response.status_code == status_code
        print("Status_code expected :", status_code, ",", self.response.status_code, "received.")
