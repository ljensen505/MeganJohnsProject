import { Container, ListGroup, Row } from "react-bootstrap";
import { Video } from "../types/Video";
import "./Videos.css";

interface VideosProps {
  videos: Video[];
}

export default function Videos(props: VideosProps) {
  const videos = props.videos;

  return (
    <section id="videos" className="content-section">
      <h2>Videos</h2>
      <Container className="videos-container">
        <Row>
          <ListGroup>
            {videos.map((video) => (
              <ListGroup.Item key={video.id} className="mb-4 video-item">
                <h4>{video.title}</h4>
                <h5>{video.subtitle}</h5>
                <Container className="youtube-player-container">
                  <div
                    dangerouslySetInnerHTML={{
                      __html: video.embedded_player_iframe,
                    }}
                  />
                </Container>
                <div
                  dangerouslySetInnerHTML={{
                    __html: video.description,
                  }}
                ></div>
              </ListGroup.Item>
            ))}
          </ListGroup>
        </Row>
      </Container>
    </section>
  );
}
