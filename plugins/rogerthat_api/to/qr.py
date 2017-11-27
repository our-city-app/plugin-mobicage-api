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
from mcfw.properties import unicode_property, typed_property, long_property
from plugins.rogerthat_api.to import ReturnStatusTO


class QRDetailsTO(TO):
    image_uri = unicode_property('1')
    content_uri = unicode_property('2')
    sms_uri = unicode_property('3')
    email_uri = unicode_property('4')


class QRReturnStatusTO(ReturnStatusTO):
    qr_details = typed_property('51', QRDetailsTO, False)


class QRTemplateTO(TO):
    id = unicode_property('1')
    description = unicode_property('2')
    color = unicode_property('3')
    timestamp = long_property('4')


class QRTemplateListResultTO(TO):
    cursor = unicode_property('1')
    templates = typed_property('2', QRTemplateTO, True)
