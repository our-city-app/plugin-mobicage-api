# -*- coding: utf-8 -*-
# Copyright 2017 GIG Technology NV
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
# @@license_version:1.3@@

from mcfw.rpc import returns, arguments, parse_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to.friends import ServiceFriendStatusTO


@returns()
@arguments(api_key=unicode, email=unicode, service_identity=unicode, app_id=unicode, json_rpc_id=unicode)
def break_up(api_key, email, service_identity=None, app_id=None, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="friend.break_up",
                   params=dict(email=email,
                               service_identity=service_identity,
                               app_id=app_id),
                   json_rpc_id=json_rpc_id)


@returns(ServiceFriendStatusTO)
@arguments(api_key=unicode, email=unicode, app_id=unicode, service_identity=unicode, json_rpc_id=unicode)
def get_status(api_key, email, app_id, service_identity=None, json_rpc_id=None):
    friend = call_rogerthat(api_key,
                            method='friend.get_status',
                            params=dict(email=email,
                                        app_id=app_id,
                                        service_identity=service_identity),
                            json_rpc_id=json_rpc_id)
    return parse_complex_value(ServiceFriendStatusTO, friend, False)
