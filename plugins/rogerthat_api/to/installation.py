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

from mcfw.properties import unicode_property, long_property, typed_property

from framework.to import TO
from plugins.rogerthat_api.plugin_utils import Enum
from plugins.rogerthat_api.to import PaginatedResultTO, UserDetailsTO
from plugins.rogerthat_api.to.system import MobileTO


class InstallationStatus(Enum):
    STARTED = 'started'
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'


class InstallationTO(TO):
    id = unicode_property('id')
    version = unicode_property('version')
    platform = unicode_property('platform')
    timestamp = long_property('timestamp')
    app_id = unicode_property('app_id')
    status = unicode_property('status')
    mobile = typed_property('mobile', MobileTO)  # type: MobileTO
    user_details = typed_property('user_details', UserDetailsTO)  # type: UserDetailsTO


class InstallationLogTO(TO):
    description = unicode_property('description')
    pin = long_property('pin')
    timestamp = long_property('timestamp')


class InstallationListTO(PaginatedResultTO):
    results = typed_property('results', InstallationTO, True)  # type: list[InstallationTO]
