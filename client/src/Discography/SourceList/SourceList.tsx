import { Album } from "../../types/Album";
import { ListGroup } from "react-bootstrap";
import SourceItem from "./SourceItem";

interface SourceListProps {
  album: Album;
}

export default function SourceList(props: SourceListProps) {
  const album = props.album;

  return (
    <ListGroup className="mb-2">
      {album.apple_music_url && (
        <SourceItem
          sourceName="Apple Music"
          sourceUrl={album.apple_music_url}
        />
      )}
      {album.spotify_url && (
        <SourceItem sourceName="Spotify" sourceUrl={album.spotify_url} />
      )}
      {album.bandcamp_url && (
        <SourceItem sourceName="Bandcamp" sourceUrl={album.bandcamp_url} />
      )}
      {album.itunes_url && (
        <SourceItem sourceName="iTunes" sourceUrl={album.itunes_url} />
      )}
    </ListGroup>
  );
}
