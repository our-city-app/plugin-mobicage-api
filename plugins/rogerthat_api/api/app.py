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

from mcfw.rpc import returns, arguments, serialize_complex_value, \
    parse_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to.app import AppSettingsTO, AppInfoTO, \
    PutLoyaltyUserResultTO, AppServiceStatisticsTO, AutoConnectedServiceTO


@returns(AppInfoTO)
@arguments(api_key=unicode, app_id=unicode, json_rpc_id=unicode)
def get_info(api_key, app_id, json_rpc_id=None):
    method = 'app.get_info'
    params = dict(app_id=app_id)
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(AppInfoTO, result, False)


@returns(AutoConnectedServiceTO)
@arguments(api_key=unicode, app_id=unicode, json_rpc_id=unicode)
def get_auto_connected_services(api_key, app_id, json_rpc_id=None):
    method = 'app.get_auto_connected_services'
    params = dict(app_id=app_id)
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(AutoConnectedServiceTO, result, True)


@returns()
@arguments(api_key=unicode, app_id=unicode, services=[AutoConnectedServiceTO], auto_connect_now=bool, json_rpc_id=unicode)
def add_auto_connected_services(api_key, app_id, services, auto_connect_now=True, json_rpc_id=None):
    method = 'app.add_auto_connected_services'
    params = dict(app_id=app_id,
                  services=services,
                  auto_connect_now=auto_connect_now)
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns()
@arguments(api_key=unicode, app_id=unicode, service_identity_email=unicode, json_rpc_id=unicode)
def delete_auto_connected_service(api_key, app_id, service_identity_email, json_rpc_id=None):
    method = 'app.delete_auto_connected_service'
    params = dict(app_id=app_id,
                  service_identity_email=service_identity_email)
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns(AppSettingsTO)
@arguments(api_key=unicode, app_id=unicode, json_rpc_id=unicode)
def get_settings(api_key, app_id=None, json_rpc_id=None):
    method = 'app.get_settings'
    params = dict()
    if app_id:
        params["app_id"] = app_id
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(AppSettingsTO, result, False)


@returns()
@arguments(api_key=unicode, settings=AppSettingsTO, app_id=unicode, json_rpc_id=unicode)
def put_settings(api_key, settings, app_id=None, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="app.put_settings",
                   params=dict(settings=serialize_complex_value(settings, AppSettingsTO, False),
                               app_id=app_id),
                   json_rpc_id=json_rpc_id)


@returns([unicode])
@arguments(api_key=unicode, app_id=unicode, amount=(int, long), json_rpc_id=unicode)
def generate_short_urls(api_key, app_id, amount, json_rpc_id=None):
    method = 'app.generate_short_urls'
    params = dict(app_id=app_id, amount=amount)
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return result


@returns(PutLoyaltyUserResultTO)
@arguments(api_key=unicode, url=unicode, email=unicode, json_rpc_id=unicode)
def put_loyalty_user(api_key, url, email, json_rpc_id=None):
    method = 'app.put_loyalty_user'
    params = dict(url=url, email=email)
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(PutLoyaltyUserResultTO, result, False)


@returns([AppServiceStatisticsTO])
@arguments(api_key=unicode, app_ids=[unicode], service_identity=unicode, json_rpc_id=unicode)
def get_statistics(api_key, app_ids, service_identity, json_rpc_id=None):
    method = 'app.get_statistics'
    params = dict(app_ids=app_ids, service_identity=service_identity)
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(AppServiceStatisticsTO, result, True)
