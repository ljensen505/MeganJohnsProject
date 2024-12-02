import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import Row from "react-bootstrap/Row";
import { Album } from "../types/Album";

interface AlbumArtworkProps {
  album: Album;
}

export default function AlbumArtwork(props: AlbumArtworkProps) {
  const album = props.album;
  const numArtworks =
    (album.front_artwork_url ? 1 : 0) + (album.rear_artwork_url ? 1 : 0);
  return (
    <Container>
      <Row>
        {album.front_artwork_url && (
          <Col xs={12} md={numArtworks === 1 ? 12 : 6}>
            <Image src={album.front_artwork_url} thumbnail />
          </Col>
        )}
        {album.rear_artwork_url && (
          <Col xs={12} md={numArtworks === 1 ? 12 : 6}>
            <Image src={album.rear_artwork_url} thumbnail />
          </Col>
        )}
      </Row>
    </Container>
  );
}
