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

from mcfw.properties import unicode_property, typed_property, long_property

from framework.to import TO
from plugins.rogerthat_api.to.messaging import AnswerTO, AttachmentTO
from plugins.rogerthat_api.to.messaging.forms import FormTO


class CallbackResultType(TO):
    pass


class MessageCallbackResultTypeTO(CallbackResultType):
    message = unicode_property('1')
    answers = typed_property('2', AnswerTO, True)
    flags = long_property('3')
    branding = unicode_property('4')
    tag = unicode_property('5')
    alert_flags = long_property('6')
    dismiss_button_ui_flags = long_property('7')
    attachments = typed_property('8', AttachmentTO, True)
    step_id = unicode_property('9')


class FormCallbackResultTypeTO(CallbackResultType):
    message = unicode_property('1')
    form = typed_property('2', FormTO, False)
    flags = long_property('3')
    alert_flags = long_property('4')
    branding = unicode_property('5')
    tag = unicode_property('6')
    attachments = typed_property('7', AttachmentTO, True)
    step_id = unicode_property('8')


class FlowCallbackResultTypeTO(CallbackResultType):
    flow = unicode_property('1')  # flow name or key or XML
    tag = unicode_property('2', default=None)
    force_language = unicode_property('3', default=None)
    flow_params = unicode_property('4', default=None)


TYPE_MESSAGE = u'message'
TYPE_FORM = u'form'
TYPE_FLOW = u'flow'
CALLBACK_RESULT_TYPE_MAPPING = {
    TYPE_MESSAGE: MessageCallbackResultTypeTO,
    TYPE_FORM: FormCallbackResultTypeTO,
    TYPE_FLOW: FlowCallbackResultTypeTO,
}


class PokeCallbackResultTO(TO):
    type = unicode_property('1')  # @ReservedAssignment
    value = typed_property('2', CallbackResultType, False, subtype_attr_name="type",
                           subtype_mapping=CALLBACK_RESULT_TYPE_MAPPING)


class MessageAcknowledgedCallbackResultTO(TO):
    type = unicode_property('1')  # @ReservedAssignment
    value = typed_property('2', CallbackResultType, False, subtype_attr_name="type",
                           subtype_mapping=CALLBACK_RESULT_TYPE_MAPPING)


class FormAcknowledgedCallbackResultTO(TO):
    type = unicode_property('1')  # @ReservedAssignment
    value = typed_property('2', CallbackResultType, False, subtype_attr_name="type",
                           subtype_mapping=CALLBACK_RESULT_TYPE_MAPPING)


class FlowMemberResultCallbackResultTO(TO):
    type = unicode_property('1')  # @ReservedAssignment
    value = typed_property('2', CallbackResultType, False, subtype_attr_name="type",
                           subtype_mapping=CALLBACK_RESULT_TYPE_MAPPING)


class FlowStartResultCallbackResultTO(TO):
    type = unicode_property('1')  # @ReservedAssignment
    value = typed_property('2', CallbackResultType, False, subtype_attr_name="type",
                           subtype_mapping=CALLBACK_RESULT_TYPE_MAPPING)


class SendApiCallCallbackResultTO(TO):
    result = unicode_property('1')
    error = unicode_property('2')
