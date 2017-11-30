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

from google.appengine.ext.deferred.deferred import PermanentTaskFailure


class BusinessException(PermanentTaskFailure):
    pass


class ServiceApiException(BusinessException):
    BASE_CODE_TEST = 2000
    BASE_CODE_BRANDING = 10000
    BASE_CODE_FRIEND = 20000
    BASE_CODE_MESSAGE = 30000
    BASE_CODE_MESSAGE_FLOW = 40000
    BASE_CODE_QR = 50000
    BASE_CODE_SERVICE = 60000
    BASE_CODE_APP = 70000
    BASE_CODE_LOCATION = 80000
    BASE_CODE_NEWS = 90000
    BASE_CODE_LOOK_AND_FEEL = 100000

    def __init__(self, code, message, **kwargs):
        super(ServiceApiException, self).__init__(message)
        self.code = code
        self._message = message
        self.fields = kwargs

    def __unicode__(self):
        return unicode(self._message)

    def __str__(self):
        return '%s - %s - %s' % (self.code, self._message, self.fields)

    def to_dict(self):
        return {'code': self.code,
                'message': self._message,
                'fields': self.fields}
