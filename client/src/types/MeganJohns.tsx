import { Album } from "./Album";
import { Artwork } from "./Artwork";
import { Bio, ProfessionalService } from "./Bio";
import { Quote } from "./Quote";
import { Video } from "./Video";

export interface MeganJohns {
  artwork: Artwork[];
  videos: Video[];
  albums: Album[];
  quotes: Quote[];
  bio: Bio;
  professional_services: ProfessionalService[];
  version: string;
}
