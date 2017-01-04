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

from mcfw.rpc import returns, arguments
from plugins.rogerthat_api.api import call_rogerthat


@returns()
@arguments(api_key=unicode, enable_on_success=bool)
def validate_callback_configuration(api_key, enable_on_success=True):
    call_rogerthat(api_key,
                   method='system.validate_callback_configuration',
                   params=dict(enable_on_success=enable_on_success))


@returns()
@arguments(api_key=unicode, function=unicode, enabled=bool)
def put_callback(api_key, function, enabled=True):
    call_rogerthat(api_key,
                   method='system.put_callback',
                   params=dict(function=function,
                               enabled=enabled))
