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

from plugins.rogerthat_api.api import RogerthatApiException
from plugins.rogerthat_api.to.news import NewsItemTO


class NewsNotFoundException(RogerthatApiException):
    def __init__(self, news_id):
        message = u'News with id %d not found' % news_id
        super(NewsNotFoundException, self).__init__(self.BASE_CODE_NEWS + 1, message)


class CannotUnstickNewsException(RogerthatApiException):
    def __init__(self):
        message = u'Cannot unstick news'
        super(CannotUnstickNewsException, self).__init__(self.BASE_CODE_NEWS + 2, message)


class TooManyNewsButtonsException(RogerthatApiException):
    def __init__(self):
        message = u'Too many news buttons. Maximum is 3 buttons, when flags are set to 0.'
        super(TooManyNewsButtonsException, self).__init__(self.BASE_CODE_NEWS + 3, message)


class CannotChangePropertyException(RogerthatApiException):
    def __init__(self, property_name):
        message = u'Property \'%s\' cannot be changed after publishing the news item.' % property_name
        super(CannotChangePropertyException, self).__init__(self.BASE_CODE_NEWS + 4, message)


class MissingNewsArgumentException(RogerthatApiException):
    def __init__(self, param):
        message = u'Parameter %s is missing' % param
        super(MissingNewsArgumentException, self).__init__(self.BASE_CODE_NEWS + 5, message)


class InvalidNewsTypeException(RogerthatApiException):
    def __init__(self, news_type):
        message = u'News type %s is not valid. Allowed types are %s' % (news_type, u', '.join(NewsItemTO.TYPES))
        super(InvalidNewsTypeException, self).__init__(self.BASE_CODE_NEWS + 6, message)


class NoPermissionToNewsException(RogerthatApiException):
    def __init__(self, requesting_user):
        message = u'You (%s) don\'t have permission to this news item.' % requesting_user
        super(NoPermissionToNewsException, self).__init__(self.BASE_CODE_NEWS + 7, message)


class ValueTooLongException(RogerthatApiException):
    def __init__(self, prop, max_length):
        message = 'The value of the property \'%s\' is too long. Only %d characters are allowed.' % (prop, max_length)
        super(ValueTooLongException, self).__init__(self.BASE_CODE_NEWS + 8, message)


class DemoServiceException(RogerthatApiException):
    def __init__(self, app_id):
        message = 'A demo service may only publish news in demo apps. %s is not a demo app.' % app_id
        super(DemoServiceException, self).__init__(self.BASE_CODE_NEWS + 9, message)


class TrialServiceException(RogerthatApiException):
    def __init__(self):
        message = 'A demo service may not publish news.'
        super(TrialServiceException, self).__init__(self.BASE_CODE_NEWS + 10, message)


class InvalidScheduledTimestamp(RogerthatApiException):
    def __init__(self):
        message = u'Scheduled timestamp must be in the future'
        super(InvalidScheduledTimestamp, self).__init__(self.BASE_CODE_NEWS + 11, message)


class CannotDeletePublishedNewsException(RogerthatApiException):
    def __init__(self, news_id):
        message = u'You cannot delete news (id %d) that has already been published.' % news_id
        super(CannotDeletePublishedNewsException, self).__init__(self.BASE_CODE_NEWS + 12, message)


class EmptyActionButtonCaption(RogerthatApiException):
    def __init__(self):
        message = u'Action button caption is empty'
        super(EmptyActionButtonCaption, self).__init__(self.BASE_CODE_NEWS + 13, message)


class InvalidActionButtonRoles(RogerthatApiException):
    def __init__(self):
        message = u'This news item is missing action button roles'
        super(InvalidActionButtonRoles, self).__init__(self.BASE_CODE_NEWS + 14, message)
