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

from plugins.rogerthat_api.models.settings import RogerthatSettings


def create_app_settings(api_key, sik, ref):
    k = RogerthatSettings.create_key(sik)
    rogerthat_settings = k.get()
    if not rogerthat_settings:
        rogerthat_settings = RogerthatSettings(key=k)

    rogerthat_settings.api_key = api_key
    rogerthat_settings.ref = ref
    rogerthat_settings.put()
