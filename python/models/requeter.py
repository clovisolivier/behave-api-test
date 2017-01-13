#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import abc


# Tool to managed http requests
class Requester(metaclass=abc.ABCMeta):

    def __init__(self,path):
        # Get params
        self.params = {}
        # Post Params
        self.body_params = {}
        # Http response
        self.response = None
        # Response Body
        self.response_body = {}
        # Service Path
        self.path = path

    # Add Get parameters
    def add_params(self, params_list):
        self.params = params_list

    # Add body Post parameters
    def add_body_request_param(self, params_list):
        self.body_params = params_list

    # Construct URL form base url
    def construct_url(self,base_url):
        return base_url + self.path

    # Call ws in Post
    def call_post_ws(self, base_url):
        url = self.construct_url(base_url)
        self.set_response(requests.post(url, data=self.body_params))
        print("Post call url", self.response.url)
        print("Body params", self.body_params)

    # Call ws in Get
    def call_get_ws(self, base_url):
        url = self.construct_url(base_url)
        self.set_response(requests.get(url, params=self.params))
        print("Get call url", self.response.url)
        print("Params", self.params)

    # Add http response
    def set_response(self, response):
        self.response = response
        assert hasattr(response, 'text')
        self.response_body = json.loads(response.text)

    # Check status code
    def assert_status_code(self, status_code):
        assert hasattr(self.response, 'status_code')
        assert self.response.status_code == status_code
        print("Status_code expected :", status_code, ",", self.response.status_code, "received.")

    # Check attributes in error
    def assert_error_attribute(self, attribute):
        assert attribute in self.response_body
        print("expected :", attribute, "not found.")