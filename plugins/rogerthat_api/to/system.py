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

from mcfw.properties import long_list_property, unicode_property, bool_property, long_property, \
    unicode_list_property, typed_property


class BaseServiceMenuItemTO(object):
    coords = long_list_property('1')
    label = unicode_property('2')
    iconHash = unicode_property('3')
    screenBranding = unicode_property('4')
    staticFlowHash = unicode_property('5', default=None)
    requiresWifi = bool_property('7', default=False)
    runInBackground = bool_property('8', default=True)


class ServiceMenuItemTO(BaseServiceMenuItemTO):
    hashedTag = unicode_property('51', default=None)


class ServicePanelMenuItemTO(ServiceMenuItemTO):
    iconName = unicode_property('50')
    iconColor = unicode_property('51')
    iconUrl = unicode_property('52')
    tag = unicode_property('53')
    staticFlowName = unicode_property('54')
    isBroadcastSettings = bool_property('55')
    roles = long_list_property('56')


class UpdatedBrandingTO(object):
    REASON_NEW_TRANSLATIONS = u'new_translations'
    old_id = unicode_property('1')
    new_id = unicode_property('2')

    @classmethod
    def create(cls, old_id, new_id):
        to = cls()
        to.old_id = old_id
        to.new_id = new_id
        return to

    @classmethod
    def from_dict(cls, d):  # d = { old_id : new_id }
        return [cls.create(*i) for i in d.iteritems()]


class ProfileLocationTO(object):
    address = unicode_property('1')
    lat = long_property('2')
    lon = long_property('3')


class SearchConfigTO(object):
    enabled = bool_property('1')
    keywords = unicode_property('2')
    locations = typed_property('3', ProfileLocationTO, True)


class BeaconTO(object):
    uuid = unicode_property('1')
    major = long_property('2')
    minor = long_property('3')
    tag = unicode_property('4', default=None)


class ServiceIdentityDetailsTO(object):
    created = long_property('1')
    identifier = unicode_property('2')
    name = unicode_property('3')
    menu_branding = unicode_property('4')
    description = unicode_property('100')
    description_use_default = bool_property('101')
    description_branding = unicode_property('102')
    description_branding_use_default = bool_property('103')
    menu_branding_use_default = bool_property('105')
    phone_number = unicode_property('106')
    phone_number_use_default = bool_property('107')
    phone_call_popup = unicode_property('108')
    phone_call_popup_use_default = bool_property('109')
    recommend_enabled = bool_property('110')
    admin_emails = unicode_list_property('111')
    search_use_default = bool_property('112')
    search_config = typed_property('113', SearchConfigTO, False)
    qualified_identifier = unicode_property('114')
    app_data = unicode_property('115')
    email_statistics_use_default = bool_property('116')
    email_statistics = bool_property('117')
    beacons = typed_property('118', BeaconTO, True)
    app_ids_use_default = bool_property('119')
    app_ids = unicode_list_property('120')
    app_names = unicode_list_property('121')
    can_edit_supported_apps = bool_property('122')
    beacon_auto_invite = bool_property('123')
    content_branding_hash = unicode_property('124')


class RoleTO(object):
    id = long_property('1')
    name = unicode_property('2')
    creation_time = long_property('3')
    type = unicode_property('4')