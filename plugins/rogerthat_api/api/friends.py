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

from mcfw.rpc import returns, arguments, parse_complex_value, serialize_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to import BaseMemberTO, UserDetailsTO
from plugins.rogerthat_api.to.friends import ServiceFriendStatusTO, \
    FriendListResultTO, SubscribedBroadcastReachTO
from plugins.rogerthat_api.to.messaging import BroadcastTargetAudienceTO


@returns()
@arguments(api_key=unicode, email=unicode, name=unicode, message=unicode, language=unicode, tag=unicode, service_identity=unicode, app_id=unicode, json_rpc_id=unicode)
def invite(api_key, email, name, message, language, tag, service_identity=None, app_id=None, json_rpc_id=None):
    method = 'friend.invite'
    params = dict(email=email,
                  name=name,
                  message=message,
                  language=language,
                  tag=tag)
    if service_identity:
        params["service_identity"] = service_identity
    if app_id:
        params["app_id"] = app_id
    call_rogerthat(api_key, method, params, json_rpc_id)


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


@returns(ServiceFriendStatusTO)
@arguments(api_key=unicode, url=unicode, service_identity=unicode, json_rpc_id=unicode)
def resolve(api_key, url, service_identity=None, json_rpc_id=None):
    method = 'friend.resolve'
    params = dict(url=url)
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(ServiceFriendStatusTO, result, False)


@returns(FriendListResultTO)
@arguments(api_key=unicode, service_identity=unicode, cursor=unicode, app_id=unicode, batch_count=(int, long), json_rpc_id=unicode)
def list_friends(api_key, service_identity=None, cursor=None, app_id=None, batch_count=100, json_rpc_id=None):
    method = 'friend.list'
    params = dict()
    if service_identity:
        params["service_identity"] = service_identity
    if cursor:
        params["cursor"] = cursor
    if app_id:
        params["app_id"] = app_id
    if batch_count:
        params["batch_count"] = batch_count
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(FriendListResultTO, result, False)


@returns([UserDetailsTO])
@arguments(api_key=unicode, search_string=unicode, service_identity=unicode, app_id=unicode, json_rpc_id=unicode)
def search_friends(api_key, search_string, service_identity=None, app_id=None, json_rpc_id=None):
    method = 'friend.search'
    params = dict(search_string=search_string)
    if service_identity:
        params["service_identity"] = service_identity
    if app_id:
        params["app_id"] = app_id
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(UserDetailsTO, result, True)


@returns(SubscribedBroadcastReachTO)
@arguments(api_key=unicode, broadcast_type=unicode, target_audience=BroadcastTargetAudienceTO, service_identity=unicode, json_rpc_id=unicode)
def get_broadcast_reach(api_key, broadcast_type, target_audience, service_identity=None, json_rpc_id=None):
    method = 'friend.get_broadcast_reach'
    params = dict(broadcast_type=broadcast_type,
                  target_audience=target_audience)
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(SubscribedBroadcastReachTO, result, False)


@returns()
@arguments(api_key=unicode, members=[BaseMemberTO], service_identities=[unicode], json_rpc_id=unicode)
def rebuild_synced_roles(api_key, members, service_identities, json_rpc_id=None):
    call_rogerthat(api_key,
                   method='friend.rebuild_synced_roles',
                   params=dict(members=serialize_complex_value(members, BaseMemberTO, True, skip_missing=True),
                               service_identities=service_identities),
                   json_rpc_id=json_rpc_id)
