import Modal from "react-bootstrap/Modal";
import { Artwork } from "../types/Artwork";
import Image from "react-bootstrap/Image";
import { Container } from "react-bootstrap";

interface ArtworkModalProps {
  artwork: Artwork;
  show: boolean;
  onHide: () => void;
}

export default function ArtworkModal(props: ArtworkModalProps) {
  const artwork = props.artwork;
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby={`{artwork.artwork_name}-centered`}
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id={`{artwork.artwork_name}-modal`}>
          {artwork.artwork_name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Container className="d-flex justify-content-center">
          <a href={artwork.source} target="_blank">
            <Image src={artwork.source} thumbnail />
          </a>
        </Container>
      </Modal.Body>
      <Modal.Footer>
        <p>
          <em>
            <small>
              {artwork.medium?.medium_name} {artwork.size} (
              {artwork.release_year})
            </small>
          </em>
        </p>
      </Modal.Footer>
    </Modal>
  );
}
