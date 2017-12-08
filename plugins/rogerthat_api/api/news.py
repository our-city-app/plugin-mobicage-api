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

from types import NoneType

from mcfw.rpc import returns, arguments, parse_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to import BaseMemberTO
from plugins.rogerthat_api.to.news import NewsItemTO, NewsItemListResultTO, \
    NewsActionButtonTO, NewsTargetAudienceTO


@returns(NewsItemTO)
@arguments(api_key=unicode, news_id=(int, long), service_identity=unicode, include_statistics=bool, json_rpc_id=unicode)
def get(api_key, news_id, service_identity=None, include_statistics=False, json_rpc_id=None):
    method = 'news.get'
    params = dict(news_id=news_id,
                  include_statistics=include_statistics)
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(NewsItemTO, result, False)


@returns(NewsItemTO)
@arguments(api_key=unicode, sticky=bool, sticky_until=(int, long), title=unicode, message=unicode, image=unicode, news_type=(int, long),
           broadcast_type=unicode, action_buttons=[NewsActionButtonTO], qr_code_content=unicode,
           qr_code_caption=unicode, scheduled_at=(int, long), flags=int, news_id=(NoneType, int, long),
           app_ids=[unicode], service_identity=unicode, target_audience=NewsTargetAudienceTO, role_ids=[(long, int)], json_rpc_id=unicode)
def publish(api_key, sticky=False, sticky_until=0, title=None, message=None, image=None, news_type=0,
            broadcast_type=None, action_buttons=None, qr_code_content=None, qr_code_caption=None,
            scheduled_at=0, flags=0, news_id=None, app_ids=None, service_identity=None,
            target_audience=None, role_ids=None, json_rpc_id=None):
    method = 'news.publish'
    params = dict(sticky=sticky,
                  sticky_until=sticky_until,
                  news_type=news_type,
                  scheduled_at=scheduled_at,
                  flags=flags)
    if title:
        params["title"] = title
    if message:
        params["message"] = message
    if image:
        params["image"] = image
    if broadcast_type:
        params["broadcast_type"] = broadcast_type
    if action_buttons:
        params["action_buttons"] = action_buttons
    if qr_code_content:
        params["qr_code_content"] = qr_code_content
    if qr_code_caption:
        params["qr_code_caption"] = qr_code_caption
    if news_id:
        params["news_id"] = news_id
    if app_ids:
        params["app_ids"] = app_ids
    if service_identity:
        params["service_identity"] = service_identity
    if target_audience:
        params["target_audience"] = target_audience
    if role_ids:
        params["role_ids"] = role_ids
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(NewsItemTO, result, False)


@returns()
@arguments(api_key=unicode, news_id=(int, long), members=[BaseMemberTO], service_identity=unicode, json_rpc_id=unicode)
def disable_news(api_key, news_id, members, service_identity=None, json_rpc_id=None):
    method = 'news.disable'
    params = dict(news_id=news_id,
                  members=members)
    if service_identity:
        params["service_identity"] = service_identity
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns(NewsItemListResultTO)
@arguments(api_key=unicode, cursor=unicode, batch_count=(int, long), service_identity=unicode, updated_since=(int, long),
           app_id=unicode, json_rpc_id=unicode)
def list_news(api_key, cursor=None, batch_count=10, service_identity=None, updated_since=0,
              app_id=None, json_rpc_id=None):
    method = 'news.list'
    params = dict(batch_count=batch_count,
                  updated_since=updated_since)
    if cursor:
        params["cursor"] = cursor
    if service_identity:
        params["service_identity"] = service_identity
    if app_id:
        params["app_id"] = app_id
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(NewsItemListResultTO, result, False)


@returns(bool)
@arguments(api_key=unicode, news_id=(int, long), service_identity=unicode, json_rpc_id=unicode)
def delete(api_key, news_id, service_identity=None, json_rpc_id=None):
    method = 'news.delete'
    params = dict(news_id=news_id)
    if service_identity:
        params["service_identity"] = service_identity
    return call_rogerthat(api_key, method, params, json_rpc_id)
