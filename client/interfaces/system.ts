export enum MobileType {
  ANDROID = 'android',
  IOS = 'ios',
  WINDOWS_PHONE = 'windows',
  BLACKBERRY = 'blackberry'
}

export const MOBILE_TYPES = {
  [ MobileType.ANDROID ]: 'rt.android',
  [ MobileType.IOS ]: 'rt.ios',
  [ MobileType.BLACKBERRY ]: 'rt.blackberry',
  [ MobileType.WINDOWS_PHONE ]: 'rt.windows_phone',
};

export interface Mobile {
  id: string;
  type: MobileType;
  description: string;
  hardware_model: string;
  registration_timestamp: string;
  os_version: string;
  language: string;
}
