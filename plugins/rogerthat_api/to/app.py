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
from mcfw.properties import bool_property, long_list_property, unicode_property, \
    long_property, unicode_list_property, typed_property


class AppInfoTO(TO):
    APP_TYPE_ROGERTHAT = 0
    APP_TYPE_CITY_APP = 1
    APP_TYPE_ENTERPRISE = 2
    APP_TYPE_CONTENT_BRANDING = 3
    APP_TYPE_YSAAA = 4

    id = unicode_property('1')
    name = unicode_property('2')
    ios_appstore_url = unicode_property('3')
    android_playstore_url = unicode_property('4')
    demo = bool_property('5')
    type = long_property('6')


class AutoConnectedServiceTO(TO):
    service_identity_email = unicode_property('1')
    removable = bool_property('2')
    local = unicode_list_property('3')
    service_roles = long_list_property('4')


class OAuthSettings(object):
    url = unicode_property('1')  # https://myoauthsite.com
    authorize_path = unicode_property('2')  # /oauth/authorize
    token_path = unicode_property('3')  # /oauth/token
    identity_path = unicode_property('4')  # /me
    scopes = unicode_property('5')  # / read,write
    client_id = unicode_property('6')
    secret = unicode_property('7')
    domain = unicode_property('8')  # myoauthsite.com
    service_identity_email = unicode_property('9')  # service@example.com
    public_key = unicode_property('10')
    jwt_audience = unicode_property('11')
    jwt_issuer = unicode_property('12')


class AppSettingsTO(TO):
    wifi_only_downloads = bool_property('1')
    background_fetch_timestamps = long_list_property('2')
    oauth = typed_property('3', OAuthSettings, False)
    birthday_message_enabled = bool_property('4')
    birthday_message = unicode_property('5')

    def __init__(self, wifi_only_downloads=None, background_fetch_timestamps=None, oauth=None,
                 birthday_message_enabled=False, birthday_message=None):
        if background_fetch_timestamps is None:
            background_fetch_timestamps = []
        self.wifi_only_downloads = wifi_only_downloads
        self.background_fetch_timestamps = background_fetch_timestamps
        self.oauth = oauth
        self.birthday_message_enabled = birthday_message_enabled
        self.birthday_message = birthday_message


class PutLoyaltyUserResultTO(TO):
    url = unicode_property('1')
    email = unicode_property('2')
    app_id = unicode_property('3')


class AppServiceStatisticsTO(TO):
    app_id = unicode_property('1')
    total_user_count = long_property('2')
