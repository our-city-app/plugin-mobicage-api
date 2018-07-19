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
from mcfw.properties import unicode_property, unicode_list_property, long_list_property, typed_property, \
    bool_property, long_property


ACCEPT_ID = u"accepted"
ACCEPT_AND_CONNECT_ID = u"accept_and_connect"
DECLINE_ID = u"decline"

REGISTRATION_ORIGIN_DEFAULT = u'default'
REGISTRATION_ORIGIN_OAUTH = u'oauth'


class RegistrationResultRolesTO(TO):
    service = unicode_property('1')  # service@example.com
    identity = unicode_property('2')  # '+default+'
    ids = long_list_property('3')  # type: list[long]


class RegistrationUserInfoTO(TO):
    name = unicode_property('name')
    avatar = unicode_property('avatar')  # base64 encoded


class RegistrationResultTO(TO):
    result = unicode_property('1')
    auto_connected_services = unicode_list_property('2')
    roles = typed_property('3', RegistrationResultRolesTO, True)
    user_details = typed_property('4', RegistrationUserInfoTO, False)  # type: RegistrationUserInfoTO


class ServiceFriendTO(TO):
    email = unicode_property('1')
    name = unicode_property('2')
    avatar = unicode_property('3')
    language = unicode_property('4')
    app_id = unicode_property('5')
    app_name = unicode_property('6')


class ServiceFriendStatusTO(ServiceFriendTO):
    is_friend = bool_property('101')
    last_heartbeat = long_property('102')


class FriendListResultTO(TO):
    cursor = unicode_property('1')
    friends = typed_property('2', ServiceFriendTO, True)  # type: list[ServiceFriendTO]
