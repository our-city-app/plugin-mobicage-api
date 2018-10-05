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

from mcfw.rpc import returns, arguments, serialize_complex_value, parse_complex_value
from plugins.rogerthat_api.api import call_rogerthat
from plugins.rogerthat_api.to import MemberTO, ChatMemberListTO
from plugins.rogerthat_api.to.messaging import AnswerTO, AttachmentTO, Message, KeyValueTO, BroadcastResultTO, \
    BroadcastTargetAudienceTO
from plugins.rogerthat_api.to.messaging.forms import FormTO


@returns(unicode)
@arguments(api_key=unicode, parent_message_key=unicode, message=unicode, answers=[AnswerTO], flags=int,
           members=[MemberTO], branding=unicode, tag=unicode, alert_flags=int, dismiss_button_ui_flags=int,
           context=unicode, attachments=[AttachmentTO], broadcast_guid=unicode, step_id=unicode, json_rpc_id=unicode)
def send(api_key, parent_message_key, message, answers, flags, members, branding, tag,
         alert_flags=Message.ALERT_FLAG_VIBRATE, dismiss_button_ui_flags=0, context=None, attachments=None,
         broadcast_guid=None, step_id=None, json_rpc_id=None):
    if attachments is None:
        attachments = []
    result = call_rogerthat(api_key,
                            method="messaging.send",
                            params=dict(parent_message_key=parent_message_key,
                                        message=message,
                                        answers=serialize_complex_value(answers, AnswerTO, True, skip_missing=True),
                                        flags=flags,
                                        members=serialize_complex_value(members, MemberTO, True, skip_missing=True),
                                        branding=branding,
                                        tag=tag,
                                        alert_flags=alert_flags,
                                        dismiss_button_ui_flags=dismiss_button_ui_flags,
                                        context=context,
                                        attachments=serialize_complex_value(attachments, AttachmentTO, True,
                                                                            skip_missing=True),
                                        broadcast_guid=broadcast_guid,
                                        step_id=step_id),
                            json_rpc_id=json_rpc_id)
    return result


@returns(unicode)
@arguments(api_key=unicode, parent_message_key=unicode, member=unicode, message=unicode, form=FormTO, flags=int,
           alert_flags=int, branding=unicode, tag=unicode, service_identity=unicode, context=unicode,
           attachments=[AttachmentTO], app_id=unicode, broadcast_guid=unicode, step_id=unicode, json_rpc_id=unicode)
def send_form(api_key, parent_message_key, member, message, form, flags, alert_flags, branding, tag,
              service_identity=None, context=None, attachments=None, app_id=None, broadcast_guid=None, step_id=None,
              json_rpc_id=None):
    if attachments is None:
        attachments = []
    result = call_rogerthat(api_key,
                            method="messaging.send_form",
                            params=dict(parent_message_key=parent_message_key,
                                        member=member,
                                        message=message,
                                        form=serialize_complex_value(form, FormTO, False, skip_missing=True),
                                        flags=flags,
                                        alert_flags=alert_flags,
                                        branding=branding,
                                        tag=tag,
                                        service_identity=service_identity,
                                        context=context,
                                        attachments=serialize_complex_value(attachments, AttachmentTO, True,
                                                                            skip_missing=True),
                                        app_id=app_id,
                                        broadcast_guid=broadcast_guid,
                                        step_id=step_id),
                            json_rpc_id=json_rpc_id)
    return result


@returns()
@arguments(api_key=unicode, parent_message_key=unicode, message_key=unicode, dirty_behavior=int, json_rpc_id=unicode)
def seal(api_key, parent_message_key, message_key, dirty_behavior=3, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="messaging.seal",
                   params=dict(parent_message_key=parent_message_key,
                               message_key=message_key,
                               dirty_behavior=dirty_behavior),
                   json_rpc_id=json_rpc_id)


@returns()
@arguments(api_key=unicode, parent_message_key=unicode, members=[MemberTO], json_rpc_id=unicode)
def delete_conversation(api_key, parent_message_key, members, json_rpc_id=None):
    call_rogerthat(api_key,
                   method="messaging.delete_conversation",
                   params=dict(parent_message_key=parent_message_key,
                               members=serialize_complex_value(members, MemberTO, True, skip_missing=True)),
                   json_rpc_id=json_rpc_id)


@returns(unicode)
@arguments(api_key=unicode, xml=unicode, members=[MemberTO], service_identity=unicode, tag=unicode,
           parent_message_key=unicode, context=unicode, force_language=unicode, download_attachments_upfront=bool,
           push_message=unicode, flow=unicode, flow_params=unicode, json_rpc_id=unicode)
def start_local_flow(api_key, xml, members, service_identity=None, tag=None, parent_message_key=None, context=None,
                     force_language=None, download_attachments_upfront=False, push_message=None, flow=None,
                     flow_params=None, json_rpc_id=None):
    return call_rogerthat(api_key,
                          method="messaging.start_local_flow",
                          params=dict(xml=xml,
                                      members=serialize_complex_value(members, MemberTO, True, skip_missing=True),
                                      service_identity=service_identity,
                                      tag=tag,
                                      parent_message_key=parent_message_key,
                                      context=context,
                                      force_language=force_language,
                                      download_attachments_upfront=download_attachments_upfront,
                                      push_message=push_message,
                                      flow=flow,
                                      flow_params=flow_params),
                          json_rpc_id=json_rpc_id)


@returns(unicode)
@arguments(api_key=unicode, members=[MemberTO], topic=unicode, description=unicode, alert_flags=(int, long),
           service_identity=unicode, tag=unicode, context=unicode, reader_members=[MemberTO], flags=(int, long),
           metadata=[KeyValueTO], avatar=unicode, background_color=unicode, text_color=unicode,
           default_priority=(int, long), default_sticky=bool, json_rpc_id=unicode)
def start_chat(api_key, members, topic, description, alert_flags=Message.ALERT_FLAG_VIBRATE, service_identity=None,
               tag=None, context=None, reader_members=None, flags=0, metadata=None, avatar=None, background_color=None,
               text_color=None, default_priority=Message.PRIORITY_NORMAL, default_sticky=False, json_rpc_id=None):
    method = 'messaging.start_chat'
    if reader_members is None:
        reader_members = list()
    if metadata is None:
        metadata = list()
    params = dict(members=serialize_complex_value(members, MemberTO, True, skip_missing=True),
                  topic=topic,
                  description=description,
                  alert_flags=alert_flags,
                  service_identity=service_identity,
                  tag=tag,
                  context=context,
                  reader_members=serialize_complex_value(reader_members, MemberTO, True, skip_missing=True),
                  flags=flags,
                  metadata=serialize_complex_value(metadata, KeyValueTO, True, skip_missing=True),
                  avatar=avatar,
                  background_color=background_color,
                  text_color=text_color,
                  default_priority=default_priority,
                  default_sticky=default_sticky)
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns(bool)
@arguments(api_key=unicode, parent_message_key=unicode, topic=unicode, description=unicode, flags=(int, long),
           metadata=[KeyValueTO], avatar=unicode, background_color=unicode, text_color=unicode, json_rpc_id=unicode)
def update_chat(api_key, parent_message_key, topic=None, description=None, flags=None, metadata=None, avatar=None,
                background_color=None, text_color=None, json_rpc_id=None):
    method = 'messaging.update_chat'
    params = {'parent_message_key': parent_message_key}
    if topic:
        params['topic'] = topic
    if description:
        params['description'] = description
    if flags:
        params['flags'] = flags
    if metadata:
        params['metadata'] = serialize_complex_value(metadata, KeyValueTO, True, skip_missing=True)
    if avatar:
        params['avatar'] = avatar
    if background_color:
        params['background_color'] = background_color
    if text_color:
        params['text_color'] = text_color

    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns(ChatMemberListTO)
@arguments(api_key=unicode, parent_message_key=unicode, cursor=unicode, json_rpc_id=unicode)
def list_chat_members(api_key, parent_message_key, cursor=None, json_rpc_id=None):
    # type: (unicode, unicode, unicode, unicode) -> ChatMemberListTO
    method = 'messaging.list_chat_members'
    params = {'parent_message_key': parent_message_key, 'cursor': cursor}
    return ChatMemberListTO.from_dict(call_rogerthat(api_key, method, params, json_rpc_id))


@returns(bool)
@arguments(api_key=unicode, parent_message_key=unicode, json_rpc_id=unicode)
def delete_chat(api_key, parent_message_key, json_rpc_id=None):
    method = 'messaging.delete_chat'
    params = {'parent_message_key': parent_message_key}
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns()
@arguments(api_key=unicode, parent_message_key=unicode, members=[MemberTO], reader_members=[MemberTO],
           json_rpc_id=unicode)
def add_chat_members(api_key, parent_message_key, members=None, reader_members=None, json_rpc_id=None):
    method = 'messaging.add_chat_members'
    if reader_members is None:
        reader_members = []
    if members is None:
        members = []
    params = dict(parent_message_key=parent_message_key,
                  members=serialize_complex_value(members, MemberTO, True, skip_missing=True),
                  reader_members=serialize_complex_value(reader_members, MemberTO, True, skip_missing=True))
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns()
@arguments(api_key=unicode, parent_message_key=unicode, members=[MemberTO], status=unicode, json_rpc_id=unicode)
def update_chat_members(api_key, parent_message_key, members, status, json_rpc_id=None):
    method = 'messaging.update_chat_members'
    params = dict(parent_message_key=parent_message_key,
                  members=serialize_complex_value(members, MemberTO, True, skip_missing=True),
                  status=status)
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns()
@arguments(api_key=unicode, parent_message_key=unicode, members=[MemberTO], soft=bool, json_rpc_id=unicode)
def delete_chat_members(api_key, parent_message_key, members=None, soft=False, json_rpc_id=None):
    method = 'messaging.delete_chat_members'
    if members is None:
        members = []
    params = dict(parent_message_key=parent_message_key,
                  members=serialize_complex_value(members, MemberTO, True, skip_missing=True),
                  soft=soft)
    return call_rogerthat(api_key, method, params, json_rpc_id)


@returns(BroadcastResultTO)
@arguments(api_key=unicode, broadcast_type=unicode, message=unicode, answers=[AnswerTO], flags=int, branding=unicode,
           tag=unicode, service_identity=unicode, alert_flags=int, dismiss_button_ui_flags=int,
           target_audience=BroadcastTargetAudienceTO, attachments=[AttachmentTO], timeout=int, json_rpc_id=unicode)
def broadcast(api_key, broadcast_type, message, answers, flags, branding, tag, service_identity=None,
              alert_flags=Message.ALERT_FLAG_VIBRATE, dismiss_button_ui_flags=0, target_audience=None, attachments=None,
              timeout=0, json_rpc_id=None):
    method = 'messaging.broadcast'
    if not attachments:
        attachments = list()
    params = dict(
        broadcast_type=broadcast_type,
        message=message,
        answers=serialize_complex_value(answers, AnswerTO, True, skip_missing=True),
        flags=flags,
        branding=branding,
        tag=tag,
        service_identity=service_identity,
        alert_flags=alert_flags,
        dismiss_button_ui_flags=dismiss_button_ui_flags,
        target_audience=serialize_complex_value(target_audience, BroadcastTargetAudienceTO, False, skip_missing=True),
        attachments=serialize_complex_value(attachments, AttachmentTO, True, skip_missing=True),
        timeout=timeout
    )
    result = call_rogerthat(api_key, method, params, json_rpc_id)
    return parse_complex_value(BroadcastResultTO, result, False)


@returns(unicode)
@arguments(api_key=unicode, parent_key=unicode, message=unicode, answers=[AnswerTO], attachments=[AttachmentTO],
           sender=(unicode, MemberTO), priority=(int, long), sticky=bool, tag=unicode, alert_flags=(int, long),
           json_rpc_id=unicode)
def send_chat_message(api_key, parent_key, message, answers=None, attachments=None, sender=None, priority=None,
                      sticky=False, tag=None, alert_flags=Message.ALERT_FLAG_VIBRATE, json_rpc_id=None):
    method = 'messaging.send_chat_message'
    if not attachments:
        attachments = list()
    if not answers:
        answers = list()
    if not priority:
        priority = 0
    params = dict(
        parent_key=parent_key,
        message=message,
        answers=serialize_complex_value(answers, AnswerTO, True, skip_missing=True),
        attachments=serialize_complex_value(attachments, AttachmentTO, True, skip_missing=True),
        sender=sender,
        priority=priority,
        sticky=sticky,
        tag=tag,
        alert_flags=alert_flags
    )
    return call_rogerthat(api_key, method, params, json_rpc_id)
