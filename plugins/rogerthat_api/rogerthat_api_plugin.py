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

from plugin_loader import Plugin
from plugins.rogerthat_api.callbacks import CallbackRequestHandler, subscribe_callback
from utils.plugins import Handler


class RogerthatApiPlugin(Plugin):

    def get_handlers(self, auth):
        if auth == Handler.AUTH_UNAUTHENTICATED:
            yield Handler(url='/plugins/rogerthat_api/callback_api', handler=CallbackRequestHandler)

    def subscribe(self, method, f):
        subscribe_callback(method, f)
