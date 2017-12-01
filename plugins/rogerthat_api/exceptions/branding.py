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


class BrandingValidationException(RogerthatApiException):
    def __init__(self, message):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_BRANDING + 0, message)


class BrandingAlreadyExistsException(RogerthatApiException):
    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_BRANDING + 1, 'Branding already exists.')


class BrandingInUseException(RogerthatApiException):
    def __init__(self, message):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_BRANDING + 2, message)


class BadBrandingZipException(RogerthatApiException):
    def __init__(self, reason):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_BRANDING + 3, 'Bad zip file', reason=reason)


class DefaultBrandingRequiredException(RogerthatApiException):
    def __init__(self):
        message = 'Cannot remove branding, a default branding is required'
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_BRANDING + 4, message)


class DefaultBrandingNotFoundExcpetion(RogerthatApiException):
    def __init__(self, branding_id):
        message = 'Default branding with id %s not found' % branding_id
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_BRANDING + 5, message)
