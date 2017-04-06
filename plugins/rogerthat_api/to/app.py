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

from mcfw.consts import MISSING
from mcfw.properties import bool_property, long_list_property


class AppSettingsTO(object):
    wifi_only_downloads = bool_property('1')
    background_fetch_timestamps = long_list_property('2')

    def __init__(self, wifi_only_downloads=MISSING, background_fetch_timestamps=MISSING):
        if wifi_only_downloads is not MISSING:
            self.wifi_only_downloads = wifi_only_downloads
        if background_fetch_timestamps is not MISSING:
            self.background_fetch_timestamps = background_fetch_timestamps
