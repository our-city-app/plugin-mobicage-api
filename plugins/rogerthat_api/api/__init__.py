# -*- coding: utf-8 -*-
# Copyright 2019 Green Valley Belgium NV
# NOTICE: THIS FILE HAS BEEN MODIFIED BY GREEN VALLEY BELGIUM NV IN ACCORDANCE WITH THE APACHE LICENSE VERSION 2.0
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
# @@license_version:1.6@@

import httplib
import json

from google.appengine.api import urlfetch

from framework.plugin_loader import get_plugin
from framework.utils import azzert, guid
from plugins.rogerthat_api.exceptions import BusinessException
from plugins.rogerthat_api.hooks import run_hook
from plugins.rogerthat_api.plugin_consts import NAMESPACE


class RogerthatApiException(BusinessException):
    def __init__(self, error_dict):
        self.fields = dict(error_dict)
        self.code = self.fields.pop('code')
        message = self.fields.pop('message')
        Exception.__init__(self, message)


class RogerthatApiStatusCodeException(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        Exception.__init__(self, 'Outgoing Rogerthat API call returned status code %s' % status_code)


class RogerthatApiUnknownException(Exception):
    def __init__(self, error):
        self.fields = error
        self.code = self.fields['code']
        super(RogerthatApiUnknownException, self).__init__(error['message'])


def call_rogerthat(api_key, method, params, json_rpc_id=None):
    # type: (unicode, unicode, dict, unicode) -> dict
    azzert(api_key, 'No API_KEY provided')
    request = {
        'id': json_rpc_id or guid(),
        'method': method,
        'params': params
    }
    run_hook('before_api_call', request)
    headers = {
        'Content-Type': 'application/json-rpc; charset=utf-8',
        'X-Nuntiuz-API-key': api_key
    }
    json_request = json.dumps(request)

    api_url = '%s/api/1' % get_plugin(NAMESPACE).configuration.rogerthat_server_url
    result = urlfetch.fetch(api_url, json_request, method=urlfetch.POST, headers=headers, deadline=600)
    if result.status_code != httplib.OK:
        raise RogerthatApiStatusCodeException(result.status_code)

    json_response = str(result.content)
    response = json.loads(json_response)
    run_hook('after_api_call', method, response)

    error = response['error']
    if error:
        if error['code'] != 1000:
            raise RogerthatApiException(error)
        else:
            raise RogerthatApiUnknownException(error)  # Unknown error (e.g. datastore timeout / transaction collision)

    return response['result']
