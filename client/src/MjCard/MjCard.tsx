/* eslint-disable no-case-declarations */
import { Button, Card } from "react-bootstrap";
import { Album } from "../types/Album";
import { Artwork } from "../types/Artwork";
import AlbumModal from "../Discography/AlbumModal";
import ArtworkModal from "../ArtworkSection/ArtworkModal";
import { useState } from "react";
import "./MjCard.css";

interface CardProps {
  type: string;
  work: Artwork | Album;
}

export default function MjCard(props: CardProps) {
  let work = props.work;
  const [show, setShow] = useState(false);

  let thumbnail: string;
  let title: string;
  let subtitle: string;

  switch (props.type) {
    case "artwork":
      work = work as Artwork;
      thumbnail = work.thumbnail;
      title = work.artwork_name;
      const medium_name = work.medium?.medium_name || "";
      const size = work?.size || "";
      subtitle = `${medium_name} ${size}`;
      break;
    case "discography":
      work = work as Album;
      thumbnail = work.front_artwork_url;
      title = work.album_name;
      subtitle = work.artist.artist_name;
      break;
    default:
      thumbnail = "";
      title = "";
      subtitle = "";
      break;
  }

  return (
    <>
      <Card className="m-3 mj-card">
        <Button
          variant="none"
          onClick={() => setShow(true)}
          className="mj-card"
        >
          <Card.Img variant="top" src={thumbnail} />
          <Card.Body>
            <Card.Title>{title}</Card.Title>
            <Card.Subtitle>{subtitle}</Card.Subtitle>
          </Card.Body>
        </Button>
      </Card>
      {props.type === "discography" && (
        <AlbumModal
          album={work as Album}
          show={show}
          onHide={() => setShow(false)}
        />
      )}
      {props.type === "artwork" && (
        <ArtworkModal
          artwork={work as Artwork}
          show={show}
          onHide={() => setShow(false)}
        />
      )}
    </>
  );
}
