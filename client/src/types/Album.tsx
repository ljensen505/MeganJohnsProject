export interface Artist {
  id: number;
  artist_name: string;
  artist_url?: string;
}

export interface Album {
  id: number;
  album_name: string;
  release_year: number;
  artist: Artist;
  front_artwork_url: string;
  spotify_url?: string;
  itunes_url?: string;
  bandcamp_url?: string;
  apple_music_url?: string;
  rear_artwork_url?: string;
  bandcamp_player?: string;
}
