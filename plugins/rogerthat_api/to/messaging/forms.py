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

from mcfw.properties import float_property, unicode_property, long_property, typed_property, unicode_list_property, \
    bool_property, long_list_property, float_list_property

from framework.to import TO
from plugins.rogerthat_api.plugin_utils import Enum
from plugins.rogerthat_api.to import PublicKeyTO
from plugins.rogerthat_api.to.messaging import MemberStatusTO, BaseMessageTO

# these dicts are populated at the bottom of this file
WIDGET_TO_MAPPING = {}
WIDGET_RESULT_TO_MAPPING = {}


class Widget(TO):
    TYPE_TEXT_LINE = u"text_line"
    TYPE_TEXT_BLOCK = u"text_block"
    TYPE_AUTO_COMPLETE = u"auto_complete"
    TYPE_FRIEND_SELECT = u"friend_select"
    TYPE_SINGLE_SELECT = u"single_select"
    TYPE_MULTI_SELECT = u"multi_select"
    TYPE_DATE_SELECT = u"date_select"
    TYPE_SINGLE_SLIDER = u"single_slider"
    TYPE_RANGE_SLIDER = u"range_slider"
    TYPE_PHOTO_UPLOAD = u"photo_upload"
    TYPE_GPS_LOCATION = u"gps_location"
    TYPE_MYDIGIPASS = u"mydigipass"
    TYPE_OPENID = u"openid"
    TYPE_ADVANCED_ORDER = u"advanced_order"
    TYPE_SIGN = u"sign"
    TYPE_OAUTH = u"oauth"
    TYPE_PAY = u"pay"


class ChoiceTO(TO):
    label = unicode_property('1')
    value = unicode_property('2')


class TextWidget(Widget):
    value = unicode_property('51')
    place_holder = unicode_property('52')
    max_chars = long_property('53')


class TextLineTO(TextWidget):
    TYPE = Widget.TYPE_TEXT_LINE


class TextBlockTO(TextWidget):
    TYPE = Widget.TYPE_TEXT_BLOCK


class AutoCompleteTO(TextWidget):
    TYPE = Widget.TYPE_AUTO_COMPLETE
    suggestions = unicode_list_property('101')


class FriendSelectTO(Widget):
    TYPE = Widget.TYPE_FRIEND_SELECT
    selection_required = bool_property('51', default=True)
    multi_select = bool_property('52', default=False)


class SelectWidget(Widget):
    choices = typed_property('51', ChoiceTO, True)


class SingleSelectTO(SelectWidget):
    TYPE = Widget.TYPE_SINGLE_SELECT
    value = unicode_property('101', empty_string_is_null=True)


class MultiSelectTO(SelectWidget):
    TYPE = Widget.TYPE_MULTI_SELECT
    values = unicode_list_property('101')


class DateSelectTO(Widget):
    TYPE = Widget.TYPE_DATE_SELECT
    MODE_TIME = u"time"
    MODE_DATE = u"date"
    MODE_DATE_TIME = u"date_time"
    MODES = (MODE_TIME, MODE_DATE, MODE_DATE_TIME)
    DEFAULT_MINUTE_INTERVAL = 15
    DEFAULT_UNIT = u"<value/>"
    date = long_property('51')
    max_date = long_property('52')
    min_date = long_property('53')
    has_date = bool_property('54')
    has_min_date = bool_property('55')
    has_max_date = bool_property('56')
    minute_interval = long_property('57')
    mode = unicode_property('58')
    unit = unicode_property('59')


class SliderWidget(Widget):
    min = float_property('51')
    max = float_property('52')
    step = float_property('53')
    unit = unicode_property('54')
    precision = long_property('55')


class SingleSliderTO(SliderWidget):
    TYPE = Widget.TYPE_SINGLE_SLIDER
    value = float_property('101')


class RangeSliderTO(SliderWidget):
    TYPE = Widget.TYPE_RANGE_SLIDER
    low_value = float_property('101')
    high_value = float_property('102')


class PhotoUploadTO(Widget):
    TYPE = Widget.TYPE_PHOTO_UPLOAD
    QUALITY_BEST = u"best"
    QUALITY_USER = u"user"
    quality = unicode_property('51')
    gallery = bool_property('52')
    camera = bool_property('53')
    ratio = unicode_property('54')


class GPSLocationTO(Widget):
    TYPE = Widget.TYPE_GPS_LOCATION
    gps = bool_property('51')


class MdpScope(Enum):
    EMAIL = u'email'
    PHONE = u'phone'
    PROFILE = u'profile'
    ADDRESS = u'address'
    EID_ADDRESS = u'eid_address'
    EID_PROFILE = u'eid_profile'
    EID_PHOTO = u'eid_photo'


class MyDigiPassTO(Widget):
    TYPE = Widget.TYPE_MYDIGIPASS
    scope = unicode_property('51', default=MdpScope.EID_PROFILE)


class AdvancedOrderItemTO(TO):
    id = unicode_property('151')
    name = unicode_property('152')
    description = unicode_property('153', default=None)
    value = long_property('154')
    unit = unicode_property('155')
    unit_price = long_property('156')
    step = long_property('157')
    step_unit = unicode_property('158', default=None)
    step_unit_conversion = long_property('159', default=0)
    image_url = unicode_property('160')
    has_price = bool_property('161', default=True)


class AdvancedOrderCategoryTO(TO):
    id = unicode_property('101')
    name = unicode_property('102')
    items = typed_property('103', AdvancedOrderItemTO, True)


class AdvancedOrderTO(Widget):
    TYPE = Widget.TYPE_ADVANCED_ORDER
    currency = unicode_property('51')
    categories = typed_property('53', AdvancedOrderCategoryTO, True)


class SignTO(Widget):
    TYPE = Widget.TYPE_SIGN
    payload = unicode_property('51')
    caption = unicode_property('52', default=None)
    algorithm = unicode_property('53', default=None)
    key_name = unicode_property('54', default=None)
    index = unicode_property('55', default=None)


class OpenIdTO(Widget):
    TYPE = Widget.TYPE_OPENID
    scope = unicode_property('scope')
    provider = unicode_property('provider')


class WidgetResult(TO):
    TYPE_UNICODE = u"unicode_result"
    TYPE_UNICODE_LIST = u"unicode_list_result"
    TYPE_LONG = u"long_result"
    TYPE_LONG_LIST = u"long_list_result"
    TYPE_FLOAT = u"float_result"
    TYPE_FLOAT_LIST = u"float_list_result"
    TYPE_LOCATION = u"location_result"
    TYPE_MYDIGIPASS = u"mydigipass_result"
    TYPE_OPENID = u"itsme"
    TYPE_ADVANCED_ORDER = u"advanced_order_result"
    TYPE_SIGN = u'sign_result'
    TYPE_PAY = u'pay_result'

    def get_value(self):
        raise NotImplementedError()


class UnicodeWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_UNICODE
    value = unicode_property('51')

    def get_value(self):
        return self.value


class UnicodeListWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_UNICODE_LIST
    values = unicode_list_property('51')

    def get_value(self):
        return self.values


class LongWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_LONG
    value = long_property('51')

    def get_value(self):
        return self.value


class LongListWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_LONG_LIST
    values = long_list_property('51')

    def get_value(self):
        return self.values


class FloatWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_FLOAT
    value = float_property('51')

    def get_value(self):
        return self.value


class FloatListWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_FLOAT_LIST
    values = float_list_property('51')

    def get_value(self):
        return self.values


class LocationWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_LOCATION
    horizontal_accuracy = float_property('51', default=-1)
    vertical_accuracy = float_property('55', default=-1)
    latitude = float_property('52')
    longitude = float_property('53')
    altitude = float_property('54')
    timestamp = long_property('56', default=0)

    def get_value(self):
        return self


class MyDigiPassEidProfile(TO):
    first_name = unicode_property('1')
    first_name_3 = unicode_property('2')
    last_name = unicode_property('3')
    gender = unicode_property('4')
    nationality = unicode_property('5')
    date_of_birth = unicode_property('6')
    location_of_birth = unicode_property('7')
    noble_condition = unicode_property('8')
    issuing_municipality = unicode_property('9')
    card_number = unicode_property('10')
    chip_number = unicode_property('11')
    validity_begins_at = unicode_property('12')
    validity_ends_at = unicode_property('13')
    created_at = unicode_property('14')


class MyDigiPassEidAddress(TO):
    street_and_number = unicode_property('1')
    zip_code = unicode_property('2')
    municipality = unicode_property('3')


class MyDigiPassProfile(TO):
    updated_at = unicode_property('1')
    first_name = unicode_property('2')
    last_name = unicode_property('3')
    born_on = unicode_property('4')
    preferred_locale = unicode_property('5')
    uuid = unicode_property('6')


class MyDigiPassAddress(TO):
    address_1 = unicode_property('1')
    address_2 = unicode_property('2')
    city = unicode_property('3')
    zip = unicode_property('4')
    country = unicode_property('5')
    state = unicode_property('6')


class MyDigiPassWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_MYDIGIPASS
    eid_profile = typed_property('50', MyDigiPassEidProfile, default=None)
    eid_address = typed_property('51', MyDigiPassEidAddress, default=None)
    eid_photo = unicode_property('52', default=None)
    email = unicode_property('53', default=None)
    phone = unicode_property('54', default=None)
    profile = typed_property('55', MyDigiPassProfile, default=None)
    address = typed_property('56', MyDigiPassAddress, default=None)

    def get_value(self):
        return self


class AdvancedOrderWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_ADVANCED_ORDER
    currency = unicode_property('50')
    categories = typed_property('51', AdvancedOrderCategoryTO, True)

    def get_value(self):
        return self


class SignWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_SIGN
    payload_signature = unicode_property('50')
    total_signature = unicode_property('51')
    public_key = typed_property('52', PublicKeyTO)

    def get_value(self):
        return self


class OpenIdAddressTO(TO):
    street_address = unicode_property('street_address', default=None)
    locality = unicode_property('locality', default=None)
    postal_code = unicode_property('postal_code', default=None)
    country = unicode_property('country', default=None)


class OpenIdWidgetResultTO(WidgetResult):
    TYPE = WidgetResult.TYPE_OPENID
    # See https://openid.net/specs/openid-connect-basic-1_0.html#rfc.section.2.5
    family_name = unicode_property('family_name', default=None)
    given_name = unicode_property('given_name', default=None)
    name = unicode_property('name', default=None)
    gender = unicode_property('gender', default=None)
    birthdate = unicode_property('birthdate', default=None)
    locale = unicode_property('locale', default=None)
    email = unicode_property('email', default=None)
    email_verified = bool_property('email_verified', default=False)
    phone_number = unicode_property('phone_number', default=None)
    phone_number_verified = bool_property('phone_number_verified', default=False)
    address = typed_property('address', OpenIdAddressTO, default=None)  # type: OpenIdAddressTO

    def get_value(self):
        return self


WIDGET_TO_MAPPING.update(
    {cls.TYPE: cls for cls in (TextLineTO, TextBlockTO, AutoCompleteTO, SingleSelectTO, MultiSelectTO, DateSelectTO,
                               FriendSelectTO, SingleSliderTO, RangeSliderTO, GPSLocationTO, PhotoUploadTO,
                               AdvancedOrderTO, SignTO, OpenIdTO)})

WIDGET_RESULT_TO_MAPPING.update(
    {cls.TYPE: cls for cls in (
        UnicodeWidgetResultTO, UnicodeListWidgetResultTO, LongWidgetResultTO, LongListWidgetResultTO,
        FloatWidgetResultTO, FloatListWidgetResultTO, LocationWidgetResultTO, AdvancedOrderWidgetResultTO,
        SignWidgetResultTO, OpenIdWidgetResultTO)})


class FormTO(TO):
    POSITIVE = u'positive'
    NEGATIVE = u'negative'
    type = unicode_property('1')  # @ReservedAssignment
    widget = typed_property('2', Widget, False, subtype_attr_name="type", subtype_mapping=WIDGET_TO_MAPPING)
    positive_button = unicode_property('3')
    negative_button = unicode_property('4')
    positive_confirmation = unicode_property('5')
    negative_confirmation = unicode_property('6')
    positive_button_ui_flags = long_property('7')
    negative_button_ui_flags = long_property('8')
    javascript_validation = unicode_property('9', default=None)

    def __init__(self, **kwargs):
        self.positive_confirmation = None
        self.negative_confirmation = None
        self.javascript_validation = None
        self.positive_button_ui_flags = 0
        self.negative_button_ui_flags = 0
        super(FormTO, self).__init__(**kwargs)


class FormMessageTO(BaseMessageTO):
    form = typed_property('51', FormTO, False)
    member = typed_property('52', MemberStatusTO, False)


class FormResultTO(TO):
    type = unicode_property('1')  # @ReservedAssignment
    result = typed_property('2', WidgetResult, False, subtype_attr_name="type",
                            subtype_mapping=WIDGET_RESULT_TO_MAPPING)


class TextLineFormTO(FormTO):
    widget = typed_property('2', TextLineTO, False)


class TextLineFormMessageTO(FormMessageTO):
    form = typed_property('51', TextLineFormTO, False)


class TextBlockFormTO(FormTO):
    widget = typed_property('2', TextBlockTO, False)


class TextBlockFormMessageTO(FormMessageTO):
    form = typed_property('51', TextBlockFormTO, False)


class AutoCompleteFormTO(FormTO):
    widget = typed_property('2', AutoCompleteTO, False)


class AutoCompleteFormMessageTO(FormMessageTO):
    form = typed_property('51', AutoCompleteFormTO, False)


class FriendSelectFormTO(FormTO):
    widget = typed_property('2', FriendSelectTO, False)


class FriendSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', FriendSelectFormTO, False)


class SingleSelectFormTO(FormTO):
    widget = typed_property('2', SingleSelectTO, False)  # type: SingleSelectTO


class SingleSelectFormMessageTO(FormMessageTO):
    """
    Args:
        form(SingleSelectFormTO)
    """
    form = typed_property('51', SingleSelectFormTO, False)


class MultiSelectFormTO(FormTO):
    widget = typed_property('2', MultiSelectTO, False)


class MultiSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', MultiSelectFormTO, False)


class DateSelectFormTO(FormTO):
    widget = typed_property('2', DateSelectTO, False)


class DateSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', DateSelectFormTO, False)


class SingleSliderFormTO(FormTO):
    widget = typed_property('2', SingleSliderTO, False)


class SingleSliderFormMessageTO(FormMessageTO):
    form = typed_property('51', SingleSliderFormTO, False)


class RangeSliderFormTO(FormTO):
    widget = typed_property('2', RangeSliderTO, False)


class RangeSliderFormMessageTO(FormMessageTO):
    form = typed_property('51', RangeSliderFormTO, False)


class PhotoUploadFormTO(FormTO):
    widget = typed_property('2', PhotoUploadTO, False)


class PhotoUploadFormMessageTO(FormMessageTO):
    form = typed_property('51', PhotoUploadFormTO, False)


class GPSLocationFormTO(FormTO):
    widget = typed_property('2', GPSLocationTO, False)


class GPSLocationFormMessageTO(FormMessageTO):
    form = typed_property('51', GPSLocationFormTO, False)


class MyDigiPassFormTO(FormTO):
    widget = typed_property('2', MyDigiPassTO, False)


class MyDigiPassFormMessageTO(FormMessageTO):
    form = typed_property('51', MyDigiPassFormTO, False)


class AdvancedOrderFormTO(FormTO):
    widget = typed_property('2', AdvancedOrderTO, False)


class AdvancedOrderFormMessageTO(FormMessageTO):
    form = typed_property('51', AdvancedOrderFormTO, False)


class SignFormTO(FormTO):
    widget = typed_property('2', SignTO, False)


class SignFormMessageTO(FormMessageTO):
    form = typed_property('51', SignFormTO, False)


class OpenIdFormTO(FormTO):
    widget = typed_property('51', OpenIdTO, False)


class OpenIdFormMessageTO(FormMessageTO):
    form = typed_property('51', OpenIdFormTO, False)
