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

from framework.to import TO
from mcfw.properties import long_list_property, unicode_property, bool_property, long_property, \
    unicode_list_property, typed_property


class ServiceIdentityInfoTO(TO):
    name = unicode_property('1')
    email = unicode_property('2')
    avatar = unicode_property('3')
    admin_emails = unicode_list_property('4')
    description = unicode_property('5')
    app_ids = unicode_list_property('6')
    app_names = unicode_list_property('7')


class BaseServiceMenuItemTO(TO):
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


class UpdatedBrandingTO(TO):
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


class ProfileLocationTO(TO):
    address = unicode_property('1')
    lat = long_property('2')
    lon = long_property('3')


class SearchConfigTO(TO):
    enabled = bool_property('1')
    keywords = unicode_property('2')
    locations = typed_property('3', ProfileLocationTO, True)


class BeaconTO(TO):
    uuid = unicode_property('1')
    major = long_property('2')
    minor = long_property('3')
    tag = unicode_property('4', default=None)


class ServiceIdentityDetailsTO(TO):
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


class RoleTO(TO):
    TYPE_MANAGED = u'managed'
    TYPE_SYNCED = u'synced'
    id = long_property('1')
    name = unicode_property('2')
    creation_time = long_property('3')
    type = unicode_property('4')


class ServiceMenuDetailItemTO(BaseServiceMenuItemTO):
    tag = unicode_property('51', default=None)


class BaseServiceMenuTO(TO):
    aboutLabel = unicode_property('2')
    messagesLabel = unicode_property('3')
    shareLabel = unicode_property('4')
    callLabel = unicode_property('5')
    callConfirmation = unicode_property('6')


class ServiceMenuDetailTO(BaseServiceMenuTO):
    items = typed_property('51', ServiceMenuDetailItemTO, True)  # type: list[ServiceMenuDetailItemTO]


class LanguagesTO(TO):
    default_language = unicode_property('1')
    supported_languages = unicode_list_property('2')


class DayStatisticsTO(TO):
    day = long_property('1')
    month = long_property('2')
    year = long_property('3')
    count = long_property('4')


class MenuItemPressTO(TO):
    name = unicode_property('1')
    data = typed_property('2', DayStatisticsTO, True)


class ServiceIdentityStatisticsTO(TO):
    number_of_users = long_property('1')
    users_gained = typed_property('2', DayStatisticsTO, True)
    users_lost = typed_property('3', DayStatisticsTO, True)
    menu_item_press = typed_property('4', MenuItemPressTO, True)


class FlowStepButtonStatisticsTO(object):
    button_id = unicode_property('1')
    acked_count = typed_property('2', DayStatisticsTO, True)

    def get_step(self, step_id):
        for step in self.steps:
            if step.step_id == step_id:
                return step
        return None


class FlowStepStatisticsTO(object):
    step_id = unicode_property('1')
    buttons = typed_property('2', FlowStepButtonStatisticsTO, True)
    sent_count = typed_property('3', DayStatisticsTO, True)
    received_count = typed_property('4', DayStatisticsTO, True)
    read_count = typed_property('5', DayStatisticsTO, True)

    def get_button(self, btn_id):
        for button in self.buttons:
            if button.button_id == btn_id:
                return button
        return None


class FlowStatisticsTO(TO):
    tag = unicode_property('1')
    flows = typed_property('2', FlowStepStatisticsTO, True, doc='Hierarchical view of steps')
    steps = typed_property('3', FlowStepStatisticsTO, True,
                           doc='Flat view of steps, containing the total sent/received/read/acked counts per day')

    def get_step(self, step_id):
        for step in self.steps:
            if step.step_id == step_id:
                return step
        return None


class FlowStatisticsListResultTO(TO):
    flow_statistics = typed_property('1', FlowStatisticsTO, True)
    cursor = unicode_property('2')
