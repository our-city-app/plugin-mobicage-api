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

from mcfw.rpc import returns, arguments, serialize_complex_value

from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to.app import AppSettingsTO
from plugins.rogerthat_api.to.installation import InstallationListTO, InstallationLogTO, InstallationTO


@returns()
@arguments(api_key=unicode, settings=AppSettingsTO, app_id=unicode, json_rpc_id=unicode)
def put_settings(api_key, settings, app_id=None, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="app.put_settings",
                   params=dict(settings=serialize_complex_value(settings, AppSettingsTO, False),
                               app_id=app_id),
                   json_rpc_id=json_rpc_id)


@returns(InstallationListTO)
@arguments(api_key=unicode, app_id=unicode, cursor=unicode, page_size=(int, long), detailed=bool, json_rpc_id=unicode)
def list_installations(api_key, app_id, cursor=None, page_size=None, detailed=False, json_rpc_id=None):
    # type: (unicode, unicode, unicode, long, unicode) -> InstallationListTO
    result = call_rogerthat(api_key,
                            method='app.list_installations',
                            params={'app_id': app_id,
                                    'cursor': cursor,
                                    'detailed': detailed,
                                    'page_size': page_size},
                            json_rpc_id=json_rpc_id)
    return InstallationListTO.from_dict(result)


@returns(InstallationTO)
@arguments(api_key=unicode, installation_id=unicode, json_rpc_id=unicode)
def get_installation(api_key, installation_id, json_rpc_id=None):
    # type: (unicode, unicode, unicode) -> InstallationTO
    result = call_rogerthat(api_key,
                            method='app.get_installation',
                            params={'installation_id': installation_id},
                            json_rpc_id=json_rpc_id)
    return InstallationTO.from_dict(result)


@returns([InstallationLogTO])
@arguments(api_key=unicode, installation_id=unicode, json_rpc_id=unicode)
def list_installation_logs(api_key, installation_id, json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method='app.list_installation_logs',
                            params={'installation_id': installation_id},
                            json_rpc_id=json_rpc_id)
    return InstallationLogTO.from_list(result)
