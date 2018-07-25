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

from mcfw.rpc import arguments
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to import BaseMemberTO
from plugins.rogerthat_api.to.friends import ServiceFriendStatusTO, FriendListResultTO


@arguments(api_key=unicode, email=unicode, service_identity=unicode, app_id=unicode, json_rpc_id=unicode)
def break_up(api_key, email, service_identity=None, app_id=None, json_rpc_id=None):
    # type: (unicode, unicode, unicode, unicode, unicode) -> None
    call_rogerthat(api_key,
                   method='friend.break_up',
                   params={
                       'email': email,
                       'service_identity': service_identity,
                       'app_id': app_id
                   },
                   json_rpc_id=json_rpc_id)


@arguments(api_key=unicode, email=unicode, app_id=unicode, service_identity=unicode, json_rpc_id=unicode)
def get_status(api_key, email, app_id, service_identity=None, json_rpc_id=None):
    # type: (unicode, unicode, unicode, unicode, unicode) -> ServiceFriendStatusTO
    friend = call_rogerthat(api_key,
                            method='friend.get_status',
                            params={
                                'email': email,
                                'app_id': app_id,
                                'service_identity': service_identity
                            },
                            json_rpc_id=json_rpc_id)
    return ServiceFriendStatusTO.from_dict(friend)


@arguments(api_key=unicode, members=[BaseMemberTO], service_identities=[unicode], json_rpc_id=unicode)
def rebuild_synced_roles(api_key, members, service_identities, json_rpc_id=None):
    # type: (unicode, list[BaseMemberTO], list[unicode], unicode) -> None
    call_rogerthat(api_key,
                   method='friend.rebuild_synced_roles',
                   params={
                       'members': [m.to_dict() for m in members],
                       'service_identities': service_identities
                   },
                   json_rpc_id=json_rpc_id)


@arguments(api_key=unicode, service_identity=unicode, cursor=unicode, app_id=unicode, batch_count=(int, long),
           json_rpc_id=unicode)
def list(api_key, service_identity=None, cursor=None, app_id=None, batch_count=1000, json_rpc_id=None):
    # type: (unicode, unicode, unicode, unicode, long, unicode) -> FriendListResultTO
    result = call_rogerthat(api_key,
                            method='friend.list',
                            params={
                                'service_identity': service_identity,
                                'cursor': cursor,
                                'app_id': app_id,
                                'batch_count': batch_count
                            },
                            json_rpc_id=json_rpc_id)
    return FriendListResultTO.from_dict(result)
