# -*- coding: utf-8 -*-
# Copyright 2017 Green IT Globe NV
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

from mcfw.rpc import returns, arguments, serialize_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to.app import AppSettingsTO


@returns()
@arguments(api_key=unicode, settings=AppSettingsTO, app_id=unicode, json_rpc_id=unicode)
def put_settings(api_key, settings, app_id=None, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="app.put_settings",
                   params=dict(settings=serialize_complex_value(settings, AppSettingsTO, False),
                               app_id=app_id),
                   json_rpc_id=json_rpc_id)
