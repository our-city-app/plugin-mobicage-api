# -*- coding: utf-8 -*-
# Copyright 2016 Mobicage NV
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
# @@license_version:1.1@@

import json
import logging

import webapp2

from plugins.rogerthat_api.models.settings import RogerthatSettings

_callbacks = {}


def subscribe_callback(method, f):
    if method in _callbacks:
        raise Exception('Already subscribed to method \'%s\'', method)
    _callbacks[method] = f


def process_callback(request, rt_settings):
    response = dict()
    method = request['method']
    id_ = request['id']
    response['id'] = id_
    logging.info('Incoming Rogerthat callback:\n%s', request)

    params = dict()
    for p, v in request['params'].iteritems():
        params[str(p)] = v

    m = _callbacks.get(method)
    if not m:
        response['result'] = None
        response['error'] = None
    else:
        try:
            response['result'] = m(rt_settings, id_, **params)
            response['error'] = None
        except Exception as e:
            response['result'] = None
            response['error'] = str(e)
            logging.exception('Incoming %s Rogerthat callback failed.', method)

    logging.debug('Response for incoming %s Rogerthat callback:\n%s', method, response)
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
