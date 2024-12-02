import axios from "axios";
import type { MeganJohns } from "./types/MeganJohns";
import type { Artwork } from "./types/Artwork";
import type { Quote } from "./types/Quote";
import type { Video } from "./types/Video";
import type { Album } from "./types/Album";
import type { Bio, ProfessionalService } from "./types/Bio";

const baseURL = import.meta.env.VITE_API_URL as string;

const api = axios.create({ baseURL: baseURL });

export const getMeganJohns = async (): Promise<MeganJohns> => {
  const response = await api.get<MeganJohns>("/");
  const albums = response.data.albums as Album[];
  const artwork = response.data.artwork as Artwork[];
  const quotes = response.data.quotes as Quote[];
  const videos = response.data.videos as Video[];
  const bio = response.data.bio as Bio;
  const professional_services = response.data
    .professional_services as ProfessionalService[];
  return {
    artwork,
    videos,
    albums,
    quotes,
    bio,
    professional_services,
  } as MeganJohns;
};
