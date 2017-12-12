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
from mcfw.properties import unicode_property, long_property, typed_property, bool_property
from plugins.oca_auth.utils.app import get_app_user_tuple


class PublicKeyTO(TO):
    algorithm = unicode_property('1', default=None)
    name = unicode_property('2', default=None)
    index = unicode_property('3', default=None)
    public_key = unicode_property('4', default=None)  # base64


class UserDetailsTO(TO):
    email = unicode_property('1')
    name = unicode_property('2')
    language = unicode_property('3')
    avatar_url = unicode_property('4')
    app_id = unicode_property('5')
    public_key = unicode_property('6')  # Deprecated
    public_keys = typed_property('7', PublicKeyTO, True, default=[])  # type: list[PublicKeyTO]

    @classmethod
    def create(cls, email, name, language, avatar_url, app_id, public_key=None, public_keys=None):
        to = cls()
        to.email = email
        to.name = name
        to.language = language
        to.avatar_url = avatar_url
        to.app_id = app_id
        to.public_key = public_key
        to.public_keys = public_keys if public_keys else []
        return to


class BaseMemberTO(TO):
    member = unicode_property('1')
    app_id = unicode_property('2')

    @classmethod
    def from_user(cls, app_user):
        memberTO = cls()
        app_user, memberTO.app_id = get_app_user_tuple(app_user)
        memberTO.member = app_user.email()
        return memberTO


class BaseButtonTO(TO):
    id = unicode_property('id')
    caption = unicode_property('caption')
    action = unicode_property('action')


class KeyValueLongTO(TO):
    key = unicode_property('1')
    value = long_property('2')

    def __init__(self, key=None, value=0):
        self.key = key
        self.value = value


class MemberTO(BaseMemberTO):
    alert_flags = long_property('3')

    @classmethod
    def from_user(cls, app_user, alert_flags=2):
        # 2 == Message.ALERT_FLAG_VIBRATE
        memberTO = super(MemberTO, cls).from_user(app_user)
        memberTO.alert_flags = alert_flags
        return memberTO


class ReturnStatusTO(TO):
    success = bool_property('1')
    errormsg = unicode_property('2')

    @classmethod
    def create(cls, success=True, errormsg=None):
        r = cls()
        r.success = success
        r.errormsg = unicode(errormsg) if errormsg else None
        return r


RETURNSTATUS_TO_SUCCESS = ReturnStatusTO.create()
