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

from mcfw.properties import unicode_property, long_property, bool_property, typed_property
from plugins.rogerthat_api.plugin_utils import Enum


class Message(object):
    TYPE = 1
    TYPE_FORM_MESSAGE = 2

    FLAG_ALLOW_DISMISS = 1
    FLAG_ALLOW_CUSTOM_REPLY = 2
    FLAG_ALLOW_REPLY = 4
    FLAG_ALLOW_REPLY_ALL = 8
    FLAG_SHARED_MEMBERS = 16
    FLAG_LOCKED = 32
    FLAG_AUTO_LOCK = 64
    FLAG_SENT_BY_MFR = 128
    FLAG_SENT_BY_JS_MFR = 256
    FLAG_DYNAMIC_CHAT = 512
    FLAG_NOT_REMOVABLE = 1024
    FLAG_ALLOW_CHAT_BUTTONS = 2048
    FLAG_CHAT_STICKY = 4096
    FLAG_ALLOW_CHAT_PICTURE = 8192
    FLAG_ALLOW_CHAT_VIDEO = 16384
    FLAG_ALLOW_CHAT_PRIORITY = 32768
    FLAG_ALLOW_CHAT_STICKY = 65536
    FLAGS = (FLAG_ALLOW_DISMISS, FLAG_ALLOW_CUSTOM_REPLY, FLAG_ALLOW_REPLY, FLAG_ALLOW_REPLY_ALL, FLAG_SHARED_MEMBERS,
             FLAG_LOCKED, FLAG_AUTO_LOCK, FLAG_SENT_BY_MFR, FLAG_SENT_BY_JS_MFR, FLAG_DYNAMIC_CHAT, FLAG_NOT_REMOVABLE,
             FLAG_ALLOW_CHAT_BUTTONS, FLAG_CHAT_STICKY, FLAG_ALLOW_CHAT_PICTURE, FLAG_ALLOW_CHAT_VIDEO,
             FLAG_ALLOW_CHAT_PRIORITY, FLAG_ALLOW_CHAT_STICKY)

    ALERT_FLAG_SILENT = 1
    ALERT_FLAG_VIBRATE = 2
    ALERT_FLAG_RING_5 = 4
    ALERT_FLAG_RING_15 = 8
    ALERT_FLAG_RING_30 = 16
    ALERT_FLAG_RING_60 = 32
    ALERT_FLAG_INTERVAL_5 = 64
    ALERT_FLAG_INTERVAL_15 = 128
    ALERT_FLAG_INTERVAL_30 = 256
    ALERT_FLAG_INTERVAL_60 = 512
    ALERT_FLAG_INTERVAL_300 = 1024
    ALERT_FLAG_INTERVAL_900 = 2048
    ALERT_FLAG_INTERVAL_3600 = 4096

    PRIORITY_NORMAL = 1
    PRIORITY_HIGH = 2
    PRIORITY_URGENT = 3
    PRIORITY_URGENT_WITH_ALARM = 4

    UI_FLAG_EXPECT_NEXT_WAIT_5 = 1
    UI_FLAG_AUTHORIZE_LOCATION = 2


class ChatFlags(Enum):
    NOT_REMOVABLE = 1
    ALLOW_ANSWER_BUTTONS = 2
    ALLOW_PICTURE = 4
    ALLOW_VIDEO = 8
    ALLOW_PRIORITY = 16
    ALLOW_STICKY = 32
    READ_ONLY = 64

    _MESSAGE_FLAG_MAPPING = {NOT_REMOVABLE: Message.FLAG_NOT_REMOVABLE,
                             ALLOW_ANSWER_BUTTONS: Message.FLAG_ALLOW_CHAT_BUTTONS,
                             ALLOW_PICTURE: Message.FLAG_ALLOW_CHAT_PICTURE,
                             ALLOW_VIDEO: Message.FLAG_ALLOW_CHAT_VIDEO,
                             ALLOW_PRIORITY: Message.FLAG_ALLOW_CHAT_PRIORITY,
                             ALLOW_STICKY: Message.FLAG_ALLOW_CHAT_STICKY,
                             READ_ONLY: -(Message.FLAG_ALLOW_REPLY | Message.FLAG_ALLOW_REPLY_ALL)}

    @classmethod
    def message_flag(cls, chat_flag):
        return cls._MESSAGE_FLAG_MAPPING[chat_flag]


class ButtonTO(object):
    id = unicode_property('1')  # @ReservedAssignment
    caption = unicode_property('2')
    action = unicode_property('3')
    ui_flags = long_property('4', default=0)


class AttachmentTO(object):
    CONTENT_TYPE_IMG_PNG = u"image/png"
    CONTENT_TYPE_IMG_JPG = u"image/jpeg"
    CONTENT_TYPE_PDF = u"application/pdf"
    CONTENT_TYPE_VIDEO_MP4 = u"video/mp4"

    CONTENT_TYPES = (CONTENT_TYPE_IMG_PNG, CONTENT_TYPE_IMG_JPG, CONTENT_TYPE_PDF, CONTENT_TYPE_VIDEO_MP4)

    content_type = unicode_property('1')
    download_url = unicode_property('2')
    name = unicode_property('3')
    size = long_property('4')


class AnswerTO(ButtonTO):
    type = unicode_property('50')  # @ReservedAssignment

    @staticmethod
    def fromButtonTO(button):
        a = AnswerTO()
        a.__dict__ = button.__dict__
        a.type = u'button'
        return a


class KeyValueTO(object):
    key = unicode_property('1')
    value = unicode_property('2')

    @classmethod
    def create(cls, key, value):
        to = cls()
        to.key = key
        to.value = value
        return to


class BroadcastResultTO(object):
    statistics_key = unicode_property('1')


class BroadcastTargetAudienceTO(object):
    min_age = long_property('0')
    max_age = long_property('1')
    gender = unicode_property('2')
    app_id = unicode_property('3')


class BaseMessageTO(object):
    key = unicode_property('1')
    parent_key = unicode_property('2')
    sender = unicode_property('3')
    message = unicode_property('5')
    flags = long_property('6')
    timestamp = long_property('9')
    branding = unicode_property('10')
    threadTimestamp = long_property('11')
    alert_flags = long_property('12')
    message_type = long_property('13')
    context = unicode_property('14')
    thread_size = long_property('15')
    broadcast_type = unicode_property('16', default=None)
    attachments = typed_property('17', AttachmentTO, True, default=[])
    thread_avatar_hash = unicode_property('18', default=None)
    thread_background_color = unicode_property('19', default=None)
    thread_text_color = unicode_property('20', default=None)
    priority = long_property('21', default=Message.PRIORITY_NORMAL)
    default_priority = long_property('22', default=Message.PRIORITY_NORMAL)
    default_sticky = bool_property('23', default=False)

    def __init__(self):
        self.context = None
        self.thread_size = 0
        self.parent_key = None


class MemberStatusTO(object):
    member = unicode_property('1')
    status = long_property('2')
    received_timestamp = long_property('3')
    acked_timestamp = long_property('4')
    button_id = unicode_property('5')
    custom_reply = unicode_property('6')


class MessageTO(BaseMessageTO):
    members = typed_property('51', MemberStatusTO, True)
    timeout = long_property('52')
    buttons = typed_property('53', ButtonTO, True)
    dismiss_button_ui_flags = long_property('54', default=0)
