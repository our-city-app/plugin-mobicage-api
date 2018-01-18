export interface PublicKey {
  algorithm: string;
  name: string;
  index: string;
  public_key: string;
}

export interface UserDetails {
  app_id: string; // 'rogerthat'
  avatar_url: string;
  email: string; // 'test@example.com
  language: string; // 'en_US'
  name: string; // 'test user'
  public_key: string | null;
  public_keys: PublicKey[];
}
