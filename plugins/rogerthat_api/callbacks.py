# -*- coding: utf-8 -*-
# Copyright 2018 Mobicage NV
# NOTICE: THIS FILE HAS BEEN MODIFIED BY MOBICAGE NV IN ACCORDANCE WITH THE APACHE LICENSE VERSION 2.0
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
# @@license_version:1.5@@

import json
import logging
from collections import defaultdict

import webapp2
from google.appengine.ext import deferred

from plugins.rogerthat_api.hooks import run_hook
from plugins.rogerthat_api.models.settings import RogerthatSettings

_callbacks = {}
_trigger_callbacks = defaultdict(list)


def subscribe_callback(method, f, trigger_only):
    if trigger_only:
        _trigger_callbacks[method].append(f)
        return

    if method in _callbacks:
        raise Exception('Already subscribed to method \'%s\'', method)
    _callbacks[method] = f


def process_callback(request, rt_settings):
    run_hook('before_callback', request)
    id_ = request['id']
    response = {
        'error': None,
        'id': id_,
        'result': None
    }
    method = request['method']
    params = {str(k): v for k, v in request['params'].iteritems()}
    callback = _callbacks.get(method)
    if callback:
        try:
            # todo: return correct TO in one parameter instead of kwargs
            response['result'] = callback(rt_settings, id_, **params)
        except Exception as e:
            response['error'] = str(e)
            logging.exception('Incoming %s Rogerthat callback failed.', method)

    if method in _trigger_callbacks:
        for f in _trigger_callbacks[method]:
            deferred.defer(f, rt_settings, id_, params, response)

    run_hook('after_callback', method, response)
    return response


class CallbackRequestHandler(webapp2.RequestHandler):
    def post(self):
        # VALIDATE THE INCOMING REQUEST
        sik = self.request.headers.get('X-Nuntiuz-Service-Key', None)
        if not sik:
            self.abort(401)
            return
        rt_settings = RogerthatSettings.create_key(sik).get()
        if not rt_settings:
            self.abort(401)
            return

        # PERFORM CALL
        response = process_callback(json.loads(self.request.body), rt_settings)

        # WIRE RESULT
        self.response.headers['Content-Type'] = 'application/json-rpc'
        json.dump(response, self.response.out)


def test_test(rt_settings, id_, value, **kwargs):
    return value


_callbacks['test.test'] = test_test
