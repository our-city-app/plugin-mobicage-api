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

from mcfw.properties import float_property
from mcfw.properties import unicode_property, long_property, typed_property, unicode_list_property, \
    bool_property, long_list_property, float_list_property
from plugins.rogerthat_api.plugin_utils import Enum
from plugins.rogerthat_api.to.messaging import MemberStatusTO, BaseMessageTO


# these dicts are populated at the bottom of this file
WIDGET_TO_MAPPING = dict()
WIDGET_RESULT_TO_MAPPING = dict()


class Widget(object):
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
    TYPE_ADVANCED_ORDER = u"advanced_order"


class FormTO(object):
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

    def __init__(self):
        self.positive_confirmation = None
        self.negative_confirmation = None
        self.javascript_validation = None
        self.positive_button_ui_flags = 0
        self.negative_button_ui_flags = 0


class FormMessageTO(BaseMessageTO):
    form = typed_property('51', FormTO, False)
    member = typed_property('52', MemberStatusTO, False)


class ChoiceTO(object):
    label = unicode_property('1')
    value = unicode_property('2')

    def __init__(self, label=None, value=None):
        self.label = label
        self.value = value

    def __str__(self):
        return "{label: %s, value: %s}" % (self.label, self.value)

    __repr__ = __str__


class TextWidget(Widget):
    value = unicode_property('51')
    place_holder = unicode_property('52')
    max_chars = long_property('53')


class TextLineTO(TextWidget):
    TYPE = Widget.TYPE_TEXT_LINE


class TextLineFormTO(FormTO):
    widget = typed_property('2', TextLineTO, False)


class TextLineFormMessageTO(FormMessageTO):
    form = typed_property('51', TextLineFormTO, False)


class TextBlockTO(TextWidget):
    TYPE = Widget.TYPE_TEXT_BLOCK


class TextBlockFormTO(FormTO):
    widget = typed_property('2', TextBlockTO, False)


class TextBlockFormMessageTO(FormMessageTO):
    form = typed_property('51', TextBlockFormTO, False)


class AutoCompleteTO(TextWidget):
    TYPE = Widget.TYPE_AUTO_COMPLETE
    suggestions = unicode_list_property('101')


class AutoCompleteFormTO(FormTO):
    widget = typed_property('2', AutoCompleteTO, False)


class AutoCompleteFormMessageTO(FormMessageTO):
    form = typed_property('51', AutoCompleteFormTO, False)


class FriendSelectTO(Widget):
    TYPE = Widget.TYPE_FRIEND_SELECT
    selection_required = bool_property('51', default=True)
    multi_select = bool_property('52', default=False)


class FriendSelectFormTO(FormTO):
    widget = typed_property('2', FriendSelectTO, False)


class FriendSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', FriendSelectFormTO, False)


class SelectWidget(Widget):
    choices = typed_property('51', ChoiceTO, True)


class SingleSelectTO(SelectWidget):
    TYPE = Widget.TYPE_SINGLE_SELECT
    value = unicode_property('101', empty_string_is_null=True)


class SingleSelectFormTO(FormTO):
    widget = typed_property('2', SingleSelectTO, False)


class SingleSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', SingleSelectFormTO, False)


class MultiSelectTO(SelectWidget):
    TYPE = Widget.TYPE_MULTI_SELECT
    values = unicode_list_property('101')


class MultiSelectFormTO(FormTO):
    widget = typed_property('2', MultiSelectTO, False)


class MultiSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', MultiSelectFormTO, False)


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


class DateSelectFormTO(FormTO):
    widget = typed_property('2', DateSelectTO, False)


class DateSelectFormMessageTO(FormMessageTO):
    form = typed_property('51', DateSelectFormTO, False)


class SliderWidget(Widget):
    min = float_property('51')
    max = float_property('52')
    step = float_property('53')
    unit = unicode_property('54')
    precision = long_property('55')


class SingleSliderTO(SliderWidget):
    TYPE = Widget.TYPE_SINGLE_SLIDER
    value = float_property('101')


class SingleSliderFormTO(FormTO):
    widget = typed_property('2', SingleSliderTO, False)


class SingleSliderFormMessageTO(FormMessageTO):
    form = typed_property('51', SingleSliderFormTO, False)


class RangeSliderTO(SliderWidget):
    TYPE = Widget.TYPE_RANGE_SLIDER
    low_value = float_property('101')
    high_value = float_property('102')


class RangeSliderFormTO(FormTO):
    widget = typed_property('2', RangeSliderTO, False)


class RangeSliderFormMessageTO(FormMessageTO):
    form = typed_property('51', RangeSliderFormTO, False)


class PhotoUploadTO(Widget):
    TYPE = Widget.TYPE_PHOTO_UPLOAD
    QUALITY_BEST = u"best"
    QUALITY_USER = u"user"
    quality = unicode_property('51')
    gallery = bool_property('52')
    camera = bool_property('53')
    ratio = unicode_property('54')


class PhotoUploadFormTO(FormTO):
    widget = typed_property('2', PhotoUploadTO, False)


class PhotoUploadFormMessageTO(FormMessageTO):
    form = typed_property('51', PhotoUploadFormTO, False)


class GPSLocationTO(Widget):
    TYPE = Widget.TYPE_GPS_LOCATION
    gps = bool_property('51')


class GPSLocationFormTO(FormTO):
    widget = typed_property('2', GPSLocationTO, False)


class GPSLocationFormMessageTO(FormMessageTO):
    form = typed_property('51', GPSLocationFormTO, False)


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


class MyDigiPassFormTO(FormTO):
    widget = typed_property('2', MyDigiPassTO, False)


class MyDigiPassFormMessageTO(FormMessageTO):
    form = typed_property('51', MyDigiPassFormTO, False)


class AdvancedOrderItemTO(object):
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


class AdvancedOrderCategoryTO(object):
    id = unicode_property('101')
    name = unicode_property('102')
    items = typed_property('103', AdvancedOrderItemTO, True)


class AdvancedOrderTO(Widget):
    TYPE = Widget.TYPE_ADVANCED_ORDER
    currency = unicode_property('51')
    categories = typed_property('53', AdvancedOrderCategoryTO, True)


class AdvancedOrderFormTO(FormTO):
    widget = typed_property('2', AdvancedOrderTO, False)


class AdvancedOrderFormMessageTO(FormMessageTO):
    form = typed_property('51', AdvancedOrderFormTO, False)


class WidgetResult(object):
    TYPE_UNICODE = u"unicode_result"
    TYPE_UNICODE_LIST = u"unicode_list_result"
    TYPE_LONG = u"long_result"
    TYPE_LONG_LIST = u"long_list_result"
    TYPE_FLOAT = u"float_result"
    TYPE_FLOAT_LIST = u"float_list_result"
    TYPE_LOCATION = u"location_result"
    TYPE_MYDIGIPASS = u"mydigipass_result"
    TYPE_ADVANCED_ORDER = u"advanced_order_result"
    TYPE_SIGN = u"sign"

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


class MyDigiPassEidProfile(object):
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


class MyDigiPassEidAddress(object):
    street_and_number = unicode_property('1')
    zip_code = unicode_property('2')
    municipality = unicode_property('3')


class MyDigiPassProfile(object):
    updated_at = unicode_property('1')
    first_name = unicode_property('2')
    last_name = unicode_property('3')
    born_on = unicode_property('4')
    preferred_locale = unicode_property('5')
    uuid = unicode_property('6')


class MyDigiPassAddress(object):
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


class SignTO(Widget):
    TYPE = WidgetResult.TYPE_SIGN
    payload = unicode_property('51')
    caption = unicode_property('52')


class SignFormTO(FormTO):
    widget = typed_property('2', SignTO, False)


class SignFormMessageTO(FormMessageTO):
    form = typed_property('51', SignFormTO, False)


class FormResultTO(object):
    type = unicode_property('1')  # @ReservedAssignment
    result = typed_property('2', WidgetResult, False, subtype_attr_name="type",
                            subtype_mapping=WIDGET_RESULT_TO_MAPPING)


WIDGET_TO_MAPPING.update(
    {cls.TYPE: cls for cls in (TextLineTO, TextBlockTO, AutoCompleteTO, SingleSelectTO, MultiSelectTO, DateSelectTO,
                               FriendSelectTO, SingleSliderTO, RangeSliderTO, GPSLocationTO, PhotoUploadTO,
                               AdvancedOrderTO, SignTO)})

WIDGET_RESULT_TO_MAPPING.update(
    {cls.TYPE: cls for cls in (
        UnicodeWidgetResultTO, UnicodeListWidgetResultTO, LongWidgetResultTO, LongListWidgetResultTO,
        FloatWidgetResultTO, FloatListWidgetResultTO, LocationWidgetResultTO, AdvancedOrderWidgetResultTO)})
