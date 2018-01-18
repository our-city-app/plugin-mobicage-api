import { UserDetails } from './service';
import { PaginatedResult } from './shared';
import { Mobile, MobileType } from './system';

export type InstallationsList = PaginatedResult<Installation>;

export enum InstallationStatus {
  STARTED = 'started',
  IN_PROGRESS = 'in_progress',
  FINISHED = 'finished'
}

export const INSTALLATION_STATUSES = {
  [ InstallationStatus.STARTED ]: 'rt.started',
  [ InstallationStatus.IN_PROGRESS ]: 'rt.in_progress',
  [ InstallationStatus.FINISHED ]: 'rt.finished',
};

export interface Installation {
  id: string;
  version: string;
  platform: MobileType;
  timestamp: number;
  app_id: string;
  status: InstallationStatus;
  mobile: Mobile | null;
  user_details: UserDetails | null;
}

export interface InstallationLog {
  description: string;
  pin: string;
  timestamp: number;
}
