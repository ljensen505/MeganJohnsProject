export interface ProfessionalService {
  id: number;
  service_name: string;
}

export interface SocialUrl {
  id: number;
  social_name: string;
  social_url: string;
}

export interface Bio {
  name: string;
  bio: string;
  social_urls: SocialUrl[];
}
