# -*- coding: utf-8 -*-
# Copyright 2016 Mobicage NV
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

from mcfw.properties import unicode_property, unicode_list_property, long_list_property, typed_property

ACCEPT_ID = u"accepted"
ACCEPT_AND_CONNECT_ID = u"accept_and_connect"
DECLINE_ID = u"decline"

REGISTRATION_ORIGIN_DEFAULT = u'default'
REGISTRATION_ORIGIN_QR = u'qr'
REGISTRATION_ORIGIN_OAUTH = u'oauth'


class RegistrationResultRolesTO(object):
    service = unicode_property('1')  # service@example.com
    identity = unicode_property('2')  # '+default+'
    ids = long_list_property('3')  # type: (list of long): role ids


class RegistrationResultTO(object):
    result = unicode_property('1')
    auto_connected_services = unicode_list_property('2')
    roles = typed_property('3', RegistrationResultRolesTO, True)
