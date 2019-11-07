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

from mcfw.properties import long_list_property, typed_property, unicode_property, long_property, bool_property

from framework.to import TO


class NavigationItemTO(TO):
    action_type = unicode_property('1')  # null, action, click, cordova
    # None means opening an activity
    # action means listing all services with that action and opening that action when clicked
    # click means clicking on a service menu item (linked to service_email).
    # If service_email is None -> the main service email is used
    # (action and click should be the hashed tag of the service menu item)
    action = unicode_property('2')  # news, messages, ...
    icon = unicode_property('3')  # font-awesome icon name
    icon_color = unicode_property('4')
    text = unicode_property('5')  # translation key
    # deprecated, should be included in params instead
    collapse = bool_property('6', default=False)
    service_email = unicode_property('7')
    params = unicode_property('8', default=None)


class ColorSettingsTO(TO):
    primary_color = unicode_property('1')
    primary_color_dark = unicode_property('2')
    primary_icon_color = unicode_property('3')
    tint_color = unicode_property('4')


class HomeScreenSettingsTO(TO):
    STYLE_NEWS = u'news'
    STYLE_MESSAGES = u'messages'

    color = unicode_property('1')
    items = typed_property('2', NavigationItemTO, True)
    style = unicode_property('3')
    header_image_url = unicode_property('4')


class ToolbarSettingsTO(TO):
    items = typed_property('1', NavigationItemTO, True)  # type: list of NavigationItemTO


class LookAndFeelTO(TO):
    colors = typed_property('1', ColorSettingsTO, False)
    homescreen = typed_property('2', HomeScreenSettingsTO, False)
    toolbar = typed_property('3', ToolbarSettingsTO, False)


class LookAndFeelServiceRolesTO(TO):
    role_ids = long_list_property('1')
    service_email = unicode_property('2')
    service_identity = unicode_property('3')


class AppLookAndFeelTO(LookAndFeelTO):
    id = long_property('50')
    app_id = unicode_property('51')
    roles = typed_property('52', LookAndFeelServiceRolesTO, True)
