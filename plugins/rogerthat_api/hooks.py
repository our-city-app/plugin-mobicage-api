# -*- coding: utf-8 -*-
# Copyright 2018 GIG Technology NV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @@license_version:1.4@@
import logging


# Default hooks log some useful info  about callbacks / api calls

def _before_callback(request):
    logging.debug('Incoming Rogerthat callback:\n%s', request)


def _after_callback(method, response):
    logging.debug('Response for incoming %s Rogerthat callback:\n%s', method, response)


def _before_api_call(request):
    logging.debug('Outgoing Rogerthat API call:\n%s', request)


def _after_api_call(method, response):
    logging.debug('Outgoing Rogerthat %s API call response:\n%s', method, response)


hooks = {
    'before_callback': _before_callback,
    'after_callback': _after_callback,
    'before_api_call': _before_api_call,
    'after_api_call': _after_api_call
}


def update_hook(hook_name, func):
    if hook_name not in hooks:
        raise Exception('Invalid hook %s, supported hooks are %s' % (hook_name, hooks.keys()))
    hooks[hook_name] = func


def run_hook(hook_name, *args, **kwargs):
    return hooks[hook_name](*args, **kwargs)
