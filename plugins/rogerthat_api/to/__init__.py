# -*- coding: utf-8 -*-
# Copyright 2018 Mobicage NV
# NOTICE: THIS FILE HAS BEEN MODIFIED BY MOBICAGE NV IN ACCORDANCE WITH THE APACHE LICENSE VERSION 2.0
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
# @@license_version:1.5@@

from framework.to import TO
from mcfw.properties import long_property, unicode_property, bool_property, typed_property


class PaginatedResultTO(TO):
    cursor = unicode_property('cursor')
    more = bool_property('more')
    results = typed_property('results', dict, True)  # Must be overwritten by superclass

    def __init__(self, cursor=None, more=False, results=None):
        super(PaginatedResultTO, self).__init__(cursor=cursor, more=more, results=results or [])


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


class BaseMemberTO(TO):
    member = unicode_property('1')
    app_id = unicode_property('2')


class MemberTO(BaseMemberTO):
    alert_flags = long_property('3')


class ReturnStatusTO(TO):
    success = bool_property('1')
    errormsg = unicode_property('2')

    @classmethod
    def create(cls, success=True, errormsg=None):
        r = cls()
        r.success = success
        r.errormsg = unicode(errormsg) if errormsg else None
        return r
