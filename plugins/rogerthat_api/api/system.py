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

import json

from mcfw.rpc import returns, arguments, parse_complex_value, serialize_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to import BaseMemberTO
from plugins.rogerthat_api.to.system import ServiceIdentityDetailsTO, RoleTO, \
    ServiceMenuDetailTO, ServiceIdentityInfoTO, LanguagesTO, \
    ServiceIdentityStatisticsTO, FlowStatisticsListResultTO


@returns(ServiceIdentityInfoTO)
@arguments(api_key=unicode, service_identity=unicode, json_rpc_id=unicode)
def get_info(api_key, service_identity=None, json_rpc_id=None):
    method = 'system.get_info'
    params = dict()
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(ServiceIdentityInfoTO, result, False)


@returns(dict)
@arguments(api_key=unicode, json_rpc_id=unicode)
def get_status(api_key, json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method="system.get_status",
                            params=dict(),
                            json_rpc_id=json_rpc_id)
    return result


@returns()
@arguments(api_key=unicode, enable_on_success=bool, callback_name=unicode, json_rpc_id=unicode)
def validate_callback_configuration(api_key, enable_on_success=True, callback_name=None, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="system.validate_callback_configuration",
                   params=dict(enable_on_success=enable_on_success,
                               callback_name=callback_name),
                   json_rpc_id=json_rpc_id)


@returns()
@arguments(api_key=unicode, json_rpc_id=unicode)
def publish_changes(api_key, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="system.publish_changes",
                   params=dict(),
                   json_rpc_id=json_rpc_id)


@returns(ServiceIdentityDetailsTO)
@arguments(api_key=unicode, service_identity=unicode, json_rpc_id=unicode)
def get_identity(api_key, service_identity=None, json_rpc_id=None):
    params = dict()
    if service_identity is not None:
        params['service_identity'] = service_identity
    si = call_rogerthat(api_key,
                        method="system.get_identity",
                        params=params,
                        json_rpc_id=json_rpc_id)
    return parse_complex_value(ServiceIdentityDetailsTO, si, False)


@returns()
@arguments(api_key=unicode, description_branding=unicode, menu_branding=unicode, app_data=dict,
           identity=ServiceIdentityDetailsTO, json_rpc_id=unicode)
def put_identity(api_key, description_branding=None, menu_branding=None, app_data=None,
                 identity=None, json_rpc_id=None):
    if not identity:
        identity = dict()
        if description_branding is not None:
            identity['description_branding'] = description_branding
        if menu_branding is not None:
            identity['menu_branding'] = menu_branding
        if app_data is not None:
            identity['app_data'] = json.dumps(app_data)
    call_rogerthat(api_key,
                   method="system.put_identity",
                   params=dict(identity=identity),
                   json_rpc_id=json_rpc_id)


@returns()
@arguments(api_key=unicode, broadcast_types=[unicode], force=bool, json_rpc_id=unicode)
def put_broadcast_types(api_key, broadcast_types, force=False, json_rpc_id=None):
    method = 'system.put_broadcast_types'
    params = dict(broadcast_types=broadcast_types,
                  force=force)
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns(dict)
@arguments(api_key=unicode, json_rpc_id=unicode)
def get_menu_item(api_key, json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method="system.get_menu_item",
                            params=dict(),
                            json_rpc_id=json_rpc_id)

    return result


@returns()
@arguments(api_key=unicode, icon_name=unicode, tag=unicode, coords=[int], icon_color=unicode, label=unicode,
           screen_branding=unicode, static_flow=unicode, json_rpc_id=unicode)
def put_menu_item(api_key, icon_name, tag, coords, icon_color, label, screen_branding=None, static_flow=None,
                  json_rpc_id=None):
    call_rogerthat(api_key,
                   method="system.put_menu_item",
                   params=dict(icon_name=icon_name,
                               tag=tag,
                               coords=coords,
                               icon_color=icon_color,
                               label=label,
                               screen_branding=screen_branding,
                               static_flow=static_flow),
                   json_rpc_id=json_rpc_id)


@returns(bool)
@arguments(api_key=unicode, coords=[int], json_rpc_id=unicode)
def delete_menu_item(api_key, coords, json_rpc_id=None):
    method = 'system.delete_menu_item'
    params = dict(coords=coords)
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns(ServiceMenuDetailTO)
@arguments(api_key=unicode, json_rpc_id=unicode)
def get_menu(api_key, json_rpc_id=None):
    method = 'system.get_menu'
    params = dict()
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(ServiceMenuDetailTO, result, False)


@returns()
@arguments(api_key=unicode, column=int, label=unicode, json_rpc_id=unicode)
def put_reserved_menu_item_label(api_key, column, label, json_rpc_id=None):
    method = 'system.put_reserved_menu_item_label'
    params = dict(column=column,
                  label=label)
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns(unicode)
@arguments(api_key=unicode, description=unicode, content=unicode, json_rpc_id=unicode)
def store_branding(api_key, description, content, json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method="system.store_branding",
                            params=dict(description=description,
                                        content=content),
                            json_rpc_id=json_rpc_id)
    return result["id"]


@returns(unicode)
@arguments(api_key=unicode, description=unicode, content=unicode, json_rpc_id=unicode)
def store_pdf_branding(api_key, description, content, json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method="system.store_pdf_branding",
                            params=dict(description=description,
                                        content=content),
                            json_rpc_id=json_rpc_id)
    return result["id"]


@returns(dict)
@arguments(api_key=unicode, email=unicode, app_id=unicode, user_data_keys=[unicode], service_identity=unicode,
           json_rpc_id=unicode)
def get_user_data(api_key, email, app_id, user_data_keys, service_identity=None, json_rpc_id=None):
    params = dict(email=email,
                  app_id=app_id,
                  user_data_keys=user_data_keys)
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key,
                            method="system.get_user_data",
                            params=params,
                            json_rpc_id=json_rpc_id)
    return json.loads(result)


@returns()
@arguments(api_key=unicode, email=unicode, app_id=unicode, user_data=dict, service_identity=unicode,
           json_rpc_id=unicode)
def put_user_data(api_key, email, app_id, user_data, service_identity=None, json_rpc_id=None):
    params = dict(email=email,
                  app_id=app_id,
                  user_data=json.dumps(user_data))
    if service_identity:
        params["service_identity"] = service_identity
    call_rogerthat(api_key,
                   method="system.put_user_data",
                   params=params,
                   json_rpc_id=json_rpc_id)


@returns()
@arguments(api_key=unicode, email=unicode, app_id=unicode, user_data_keys=[unicode], service_identity=unicode,
           json_rpc_id=unicode)
def del_user_data(api_key, email, app_id, user_data_keys, service_identity=None, json_rpc_id=None):
    params = dict(email=email,
                  app_id=app_id,
                  user_data_keys=user_data_keys)
    if service_identity:
        params["service_identity"] = service_identity
    call_rogerthat(api_key,
                   method='system.del_user_data',
                   params=params,
                   json_rpc_id=json_rpc_id)


@returns(unicode)
@arguments(api_key=unicode, xml=unicode, multilanguage=bool, json_rpc_id=unicode)
def put_flow(api_key, xml, multilanguage=True, json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method="system.put_flow",
                            params=dict(xml=xml,
                                        multilanguage=multilanguage),
                            json_rpc_id=json_rpc_id)

    return result['identifier']


@returns(LanguagesTO)
@arguments(api_key=unicode, app_id=unicode, json_rpc_id=unicode)
def get_languages(api_key, app_id=None, json_rpc_id=None):
    method = 'system.get_languages'
    params = dict()
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(LanguagesTO, result, False)


@returns()
@arguments(api_key=unicode, base64_image=unicode, json_rpc_id=unicode)
def put_avatar(api_key, base64_image, json_rpc_id=None):
    call_rogerthat(api_key=api_key,
                   method="system.put_avatar",
                   params=dict(image=base64_image),
                   json_rpc_id=json_rpc_id)


@returns(unicode)
@arguments(api_key=unicode, json_rpc_id=unicode)
def get_avatar(api_key, json_rpc_id=None):
    method = 'system.put_avatar'
    params = dict()
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns(ServiceIdentityStatisticsTO)
@arguments(api_key=unicode, service_identity=unicode, json_rpc_id=unicode)
def get_statistics(api_key, service_identity=None, json_rpc_id=None):
    method = 'system.get_statistics'
    params = dict()
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(ServiceIdentityStatisticsTO, result, False)


@returns(FlowStatisticsListResultTO)
@arguments(api_key=unicode, tags=[unicode], views=(int, long), time_span=(int, long), group_by=unicode, cursor=unicode,
           service_identity=unicode, json_rpc_id=unicode)
def get_flow_statistics(api_key, tags, views, time_span, group_by=None, cursor=None, service_identity=None, json_rpc_id=None):
    method = 'system.get_flow_statistics'
    params = dict(tags=tags,
                  views=views,
                  time_span=time_span)
    if group_by:
        params["group_by"] = group_by
    if cursor:
        params["cursor"] = cursor
    if service_identity:
        params["service_identity"] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(FlowStatisticsListResultTO, result, False)


@returns(unicode)
@arguments(api_key=unicode, service_identity=unicode, json_rpc_id=unicode)
def export_flow_statistics(api_key, service_identity=None, json_rpc_id=None):
    method = 'system.export_flow_statistics'
    params = dict()
    if service_identity:
        params["service_identity"] = service_identity
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns(long)
@arguments(api_key=unicode, name=unicode, role_type=unicode, json_rpc_id=unicode)
def put_role(api_key, name, role_type, json_rpc_id=None):
    return call_rogerthat(api_key=api_key,
                          method="system.put_role",
                          params=dict(name=name,
                                      role_type=role_type),
                          json_rpc_id=json_rpc_id)


@returns()
@arguments(api_key=unicode, role_id=(int, long), cleanup_members=bool, json_rpc_id=unicode)
def delete_role(api_key, role_id, cleanup_members=False, json_rpc_id=None):
    method = 'system.delete_role'
    params = dict(role_id=role_id,
                  cleanup_members=cleanup_members)
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns()
@arguments(api_key=unicode, role_id=(int, long), member=BaseMemberTO, service_identity=unicode, json_rpc_id=unicode)
def add_role_member(api_key, role_id, member, service_identity=None, json_rpc_id=None):
    call_rogerthat(api_key=api_key,
                   method="system.add_role_member",
                   params=dict(role_id=role_id,
                               member=serialize_complex_value(member, BaseMemberTO, False, skip_missing=True),
                               service_identity=service_identity),
                   json_rpc_id=json_rpc_id)


@returns()
@arguments(api_key=unicode, role_id=(int, long), member=BaseMemberTO, service_identity=unicode, json_rpc_id=unicode)
def delete_role_member(api_key, role_id, member, service_identity=None, json_rpc_id=None):
    call_rogerthat(api_key=api_key,
                   method="system.delete_role_member",
                   params=dict(role_id=role_id,
                               member=serialize_complex_value(member, BaseMemberTO, False, skip_missing=True),
                               service_identity=service_identity),
                   json_rpc_id=json_rpc_id)


@returns([RoleTO])
@arguments(api_key=unicode, json_rpc_id=unicode)
def list_roles(api_key, json_rpc_id=None):
    roles = call_rogerthat(api_key, method="system.list_roles", params=dict(), json_rpc_id=json_rpc_id)
    return parse_complex_value(RoleTO, roles, True)


@returns(dict)
@arguments(api_key=unicode, service_data_keys=[unicode], service_identity=unicode,
           json_rpc_id=unicode)
def get_service_data(api_key, service_data_keys, service_identity=None, json_rpc_id=None):
    method = 'system.get_service_data'
    params = dict(
        keys=service_data_keys
    )
    if service_identity:
        params['service_identity'] = service_identity
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return json.loads(result)


@returns()
@arguments(api_key=unicode, data=dict, service_identity=unicode, json_rpc_id=unicode)
def put_service_data(api_key, data, service_identity=None, json_rpc_id=None):
    method = 'system.put_service_data'
    params = dict(
        data=json.dumps(data)
    )
    if service_identity:
        params['service_identity'] = service_identity
    call_rogerthat(api_key, method, params, json_rpc_id)


@returns()
@arguments(api_key=unicode, function=unicode, enabled=bool, json_rpc_id=unicode)
def put_callback(api_key, function, enabled=True, json_rpc_id=None):
    call_rogerthat(api_key,
                   method='system.put_callback',
                   params=dict(function=function,
                               enabled=enabled),
                   json_rpc_id=json_rpc_id)
