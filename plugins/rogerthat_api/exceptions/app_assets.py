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


class AppAssetNotFoundException(RogerthatApiException):
    def __init__(self, asset_id):
        code = RogerthatApiException.BASE_CODE_APP + 100
        data = {
            'asset_id': asset_id
        }
        super(AppAssetNotFoundException, self).__init__(code, 'app_asset_not_found', data)


class CannotDeleteDefaultAppAssetException(RogerthatApiException):
    def __init__(self):
        code = RogerthatApiException.BASE_CODE_APP + 101
        super(CannotDeleteDefaultAppAssetException, self).__init__(code, 'cannot_delete_default_app_asset')
