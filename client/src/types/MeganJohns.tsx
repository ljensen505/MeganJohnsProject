import type { Album } from "./Album";
import type { Artwork } from "./Artwork";
import type { Bio, ProfessionalService } from "./Bio";
import type { Quote } from "./Quote";
import type { Video } from "./Video";

export interface MeganJohns {
  artwork: Artwork[];
  videos: Video[];
  albums: Album[];
  quotes: Quote[];
  bio: Bio;
  professional_services: ProfessionalService[];
}
