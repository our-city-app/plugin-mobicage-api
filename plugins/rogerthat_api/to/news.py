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
from mcfw.properties import long_property, typed_property, unicode_property, \
    bool_property, unicode_list_property, long_list_property
from plugins.rogerthat_api.to import BaseButtonTO, KeyValueLongTO


class NewsSenderTO(TO):
    email = unicode_property('1')
    name = unicode_property('2')
    avatar_id = long_property('3')


class NewsActionButtonTO(BaseButtonTO):
    flow_params = unicode_property('101')


class NewsItemStatisticsTimeTO(TO):
    timestamp = long_property('1')
    amount = long_property('2')


class NewsItemStatisticsDetailsTO(TO):
    age = typed_property('1', KeyValueLongTO, True)  # key: age (e.g. 10 - 15), value: amount
    gender = typed_property('2', KeyValueLongTO, True)  # key: gender, value: amount
    time = typed_property('3', NewsItemStatisticsTimeTO, True)
    total = long_property('4')


class NewsItemStatisticsTO(TO):
    app_id = unicode_property('1')
    reached = typed_property('2', NewsItemStatisticsDetailsTO, False)
    rogered = typed_property('3', NewsItemStatisticsDetailsTO, False)
    action = typed_property('4', NewsItemStatisticsDetailsTO, False)
    followed = typed_property('5', NewsItemStatisticsDetailsTO, False)


class NewsTargetAudienceTO(TO):
    min_age = long_property('1', default=0)
    max_age = long_property('2', default=200)
    gender = long_property('3', default=0)  # GENDER_MALE_OR_FEMALE
    connected_users_only = bool_property('4', default=False)


class BaseNewsItemTO(TO):
    id = long_property('1')
    sender = typed_property('2', NewsSenderTO, False)
    title = unicode_property('3')
    message = unicode_property('4')
    image_url = unicode_property('5')
    broadcast_type = unicode_property('6')
    reach = long_property('7')
    users_that_rogered = unicode_list_property('8')
    buttons = typed_property('9', NewsActionButtonTO, True)
    qr_code_content = unicode_property('10')
    qr_code_caption = unicode_property('11')
    version = long_property('12')
    timestamp = long_property('13')
    flags = long_property('14')
    type = long_property('15')


class NewsItemTO(BaseNewsItemTO):
    TYPE_NORMAL = 1
    TYPE_QR_CODE = 2
    TYPES = (TYPE_QR_CODE, TYPE_NORMAL)

    MAX_TITLE_LENGTH = 80
    MAX_BUTTON_CAPTION_LENGTH = 15

    FLAG_ACTION_ROGERTHAT = 1
    FLAG_ACTION_FOLLOW = 2
    FLAG_SILENT = 4
    DEFAULT_FLAGS = FLAG_ACTION_FOLLOW | FLAG_ACTION_ROGERTHAT

    MAX_BUTTON_COUNT = 3

    sticky = bool_property('101')
    sticky_until = long_property('102')
    app_ids = unicode_list_property('103')
    rogered = bool_property('104')
    scheduled_at = long_property('105')
    published = bool_property('106')
    statistics = typed_property('107', NewsItemStatisticsTO, True)
    action_count = long_property('108')
    follow_count = long_property('109')

    target_audience = typed_property('110', NewsTargetAudienceTO, False)
    role_ids = long_list_property('111', default=[])


class NewsItemListResultTO(TO):
    result = typed_property('1', NewsItemTO, True)
    cursor = unicode_property('2')
