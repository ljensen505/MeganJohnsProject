import { Modal } from "react-bootstrap";
import { Album } from "../types/Album";
import SourceList from "./SourceList/SourceList";
import AlbumArtwork from "./AlbumArtwork";

interface AlbumModalProps {
  album: Album;
  show: boolean;
  onHide: () => void;
}

export default function AlbumModal(props: AlbumModalProps) {
  const album = props.album;
  const bandcampPlayer = album.bandcamp_player ? (
    <div
      dangerouslySetInnerHTML={{
        __html: album.bandcamp_player,
      }}
    />
  ) : null;

  const handleClose = () => {
    props.onHide();
  };

  return (
    <Modal {...props} onHide={handleClose} size="lg" centered>
      <Modal.Header closeButton>
        <Modal.Title id={`{album.album_name}-modal`}>
          {album.album_name}
        </Modal.Title>
      </Modal.Header>
      <AlbumArtwork album={album} />
      <Modal.Body>
        <SourceList album={album} />
        {bandcampPlayer}
      </Modal.Body>
      <Modal.Footer>
        {album.artist.artist_name} ({album.release_year})
      </Modal.Footer>
    </Modal>
  );
}
