// class Medium {
//   id: number;
//   medium_name: string;

//   constructor(id: number, medium_name: string) {
//     this.id = id;
//     this.medium_name = medium_name;
//   }
// }

export interface Medium {
  id: number;
  medium_name: string;
}

export interface Artwork {
  id: number;
  artwork_name: string;
  source: string;
  thumbnail: string;
  is_featured: boolean;
  medium?: Medium;
  release_year?: number;
  size?: string;
}

// class Artwork {
//   id: number;
//   type: string = "artwork";
//   artwork_name: string;
//   medium: Medium;
//   source_url: string;
//   release_year: string;
//   size?: string;

//   constructor(
//     id: number,
//     artwork_name: string,
//     medium: Medium,
//     source_url: string,
//     release_year: string,
//     size?: string
//   ) {
//     this.id = id;
//     this.type = "artwork";
//     this.artwork_name = artwork_name;
//     this.medium = medium;
//     this.source_url = source_url;
//     this.release_year = release_year;
//     this.size = size;
//   }
// }
