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

from __future__ import unicode_literals

import logging

from framework.plugin_loader import Plugin
from framework.utils.plugins import Handler
from mcfw.consts import MISSING, DEBUG
from mcfw.rpc import parse_complex_value
from plugins.rogerthat_api.callbacks import CallbackRequestHandler, subscribe_callback
from plugins.rogerthat_api.hooks import update_hook
from plugins.rogerthat_api.to.config import RogerthatApiPluginConfiguration


class RogerthatApiPlugin(Plugin):
    def __init__(self, configuration):
        super(RogerthatApiPlugin, self).__init__(configuration)
        self.configuration = parse_complex_value(RogerthatApiPluginConfiguration,
                                                 configuration if configuration is not MISSING else {},
                                                 False)  # type: RogerthatApiPluginConfiguration
        if self.configuration.rogerthat_server_url is MISSING \
            or not self.configuration.rogerthat_server_url \
                or self.configuration.rogerthat_server_url == 'https://rogerth.at':
            logging.warn('[RogerthatApiPlugin]: Set the \'rogerthat_server_url\' in the configuration file'
                         'to an appengine application url (<project-id>.appspot.com) to decrease the latency of the'
                         ' requests to rogerthat.')
            self.configuration.rogerthat_server_url = 'https://rogerth.at'
        elif 'localhost' in self.configuration.rogerthat_server_url and not DEBUG:
            logging.error('Invalid rogerthat_server_url %s', self.configuration.rogerthat_server_url)

    def get_handlers(self, auth):
        if auth == Handler.AUTH_UNAUTHENTICATED:
            yield Handler(url='/plugins/rogerthat_api/callback_api', handler=CallbackRequestHandler)

    def subscribe(self, method, f, trigger_only=False):
        subscribe_callback(method, f, trigger_only)

    def set_hook(self, hook_name, func):
        update_hook(hook_name, func)
