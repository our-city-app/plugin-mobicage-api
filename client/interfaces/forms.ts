import { PublicKey } from './service';

export enum FlowStepType {
  MESSAGE = 'message_step',
  FORM = 'form_step',
}

export enum WidgetResultType {
  UNICODE = 'unicode_result',
  UNICODE_LIST = 'unicode_list_result',
  LONG = 'long_result',
  LONG_LIST = 'long_list_result',
  FLOAT = 'float_result',
  FLOAT_LIST = 'float_list_result',
  LOCATION = 'location_result',
  MYDIGIPASS = 'mydigipass_result',
  ADVANCED_ORDER = 'advanced_order_result',
  SIGN = 'sign_result',
}

export enum WidgetType {
  TEXT_LINE = 'text_line',
  TEXT_BLOCK = 'text_block',
  AUTO_COMPLETE = 'auto_complete',
  FRIEND_SELECT = 'friend_select',
  SINGLE_SELECT = 'single_select',
  MULTI_SELECT = 'multi_select',
  DATE_SELECT = 'date_select',
  SINGLE_SLIDER = 'single_slider',
  RANGE_SLIDER = 'range_slider',
  PHOTO_UPLOAD = 'photo_upload',
  GPS_LOCATION = 'gps_location',
  MYDIGIPASS = 'mydigipass',
  ADVANCED_ORDER = 'advanced_order',
  SIGN = 'sign',
  OAUTH = 'oauth',
}

export interface BaseFlowStep {
  step_id: string;
  message_flow_id: string;
  received_timestamp: number;
  acknowledged_timestamp: number;
  step_type: FlowStepType;
  answer_id: string;
  message: string;
  button: string;
}

export interface FormFlowStep extends BaseFlowStep {
  step_type: FlowStepType.FORM;
  form_result: FormResult | null;
  display_value: string | null;
  form_type: WidgetType;
}

export interface MessageFlowStep extends BaseFlowStep {
  step_type: FlowStepType.MESSAGE;
}

export type FlowStep = FormFlowStep | MessageFlowStep;

export interface UnicodeWidgetResult {
  value: string;
}

export interface UnicodeListWidgetResult {
  values: string[];
}

export interface LongWidgetResult {
  value: number;
}

export interface LongListWidgetResult {
  values: number[];
}

export interface LocationWidgetResult {
  horizontal_accuracy: number;
  vertical_accuracy: number;
  latitude: number;
  longitude: number;
  altitude: number;
  timestamp: number;
}

export interface MyDigiPassWidgetResult {
  eid_profile: {
    first_name: string;
    first_name_3: string;
    last_name: string;
    gender: string;
    nationality: string;
    date_of_birth: string;
    location_of_birth: string;
    noble_condition: string;
    issuing_municipality: string;
    card_number: string;
    chip_number: string;
    validity_begins_at: string;
    validity_ends_at: string;
    created_at: string;
  };
  eid_address: {
    street_and_number: string;
    zip_code: string;
    municipality: string;
  };
  eid_photo: string;
  email: string;
  phone: string;
  profile: {
    updated_at: string;
    first_name: string;
    last_name: string;
    born_on: string;
    preferred_locale: string;
    uuid: string;
  };
  address: {
    address_1: string;
    address_2: string;
    city: string;
    zip: string;
    country: string;
    state: string;
  };
}

export interface AdvancedOrderItem {
  id: string;
  name: string;
  description: string;
  value: number;
  unit: string;
  unit_price: number;
  step: number;
  step_unit: string;
  step_unit_conversion: number;
  image_url: string;
  has_price: boolean;
}

export interface AdvancedOrderCategory {
  id: string;
  name: string;
  items: AdvancedOrderItem[];
}

export interface AdvancedOrderWidgetResult {
  currency: string;
  categories: AdvancedOrderCategory[];
}

export interface SignWidgetResult {
  payload_signature: string;
  total_signature: string;
  public_key: PublicKey;
}

export interface FormResultUnicodeWidget {
  type: WidgetResultType.UNICODE;
  result: UnicodeWidgetResult;
}

export interface FormResultUnicodeListWidget {
  type: WidgetResultType.UNICODE_LIST;
  result: UnicodeListWidgetResult;
}

export interface FormResultLongWidget {
  type: WidgetResultType.LONG;
  result: LongWidgetResult;
}

export interface FormResultLongListWidget {
  type: WidgetResultType.LONG_LIST;
  result: LongListWidgetResult;
}

export interface FormResultFloatWidget {
  type: WidgetResultType.FLOAT;
  result: LongWidgetResult;
}

export interface FormResultFloatListWidget {
  type: WidgetResultType.FLOAT_LIST;
  result: LongListWidgetResult;
}

export interface FormResultLocationWidget {
  type: WidgetResultType.LOCATION;
  result: LocationWidgetResult;
}

export interface FormResultMyDigiPassWidget {
  type: WidgetResultType.MYDIGIPASS;
  result: MyDigiPassWidgetResult;
}

export interface FormResultAdvancedOrderWidget {
  type: WidgetResultType.ADVANCED_ORDER;
  result: AdvancedOrderWidgetResult;
}

export interface FormResultSignWidget {
  type: WidgetResultType.SIGN;
  result: SignWidgetResult;
}

export type FormResult = FormResultUnicodeWidget |
  FormResultUnicodeListWidget |
  FormResultFloatWidget |
  FormResultLongWidget |
  FormResultLongListWidget |
  FormResultFloatWidget |
  FormResultFloatListWidget |
  FormResultLocationWidget |
  FormResultMyDigiPassWidget |
  FormResultAdvancedOrderWidget |
  FormResultSignWidget;
