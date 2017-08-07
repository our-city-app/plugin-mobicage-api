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

from mcfw.rpc import returns, arguments, parse_complex_value
from plugins.rogerthat_api.to.qr import QRDetailsTO
from plugins.rogerthat_api.api import call_rogerthat


@returns(QRDetailsTO)
@arguments(api_key=unicode, description=unicode, tag=unicode, template_key=unicode, service_identity=unicode, 
           flow=unicode, branding=unicode, json_rpc_id=unicode)
def create(api_key, description, tag, template_key=None, service_identity=None, flow=None, branding=None, 
           json_rpc_id=None):
    result = call_rogerthat(api_key,
                            method='qr.create',
                            params=dict(description=description,
                                        tag=tag,
                                        template_key=template_key,
                                        service_identity=service_identity,
                                        flow=flow,
                                        branding=branding),
                            json_rpc_id=json_rpc_id)
    return parse_complex_value(QRDetailsTO, result, False)
