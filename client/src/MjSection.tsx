// import { Album } from "./types/Album";
import { Col, Container, Row } from "react-bootstrap";
import { Artwork } from "./types/Artwork";
import MjCard from "./MjCard/MjCard";
import { Album } from "./types/Album";

interface MjSectionProps {
  sectionTitle: string;
  works: Artwork[] | Album[];
}

export default function MjSection(props: MjSectionProps) {
  const sectionTitleAsTitle =
    props.sectionTitle.charAt(0).toUpperCase() + props.sectionTitle.slice(1);
  const works = props.works;
  return (
    <section id={props.sectionTitle} className="content-section">
      <h2>{sectionTitleAsTitle}</h2>
      <Container>
        <Row>
          {works.map((work) => (
            <Col
              key={`${props.sectionTitle}-${work.id}`}
              className="d-flex justify-content-center align-items-center"
            >
              <MjCard type={props.sectionTitle} work={work} />
            </Col>
          ))}
        </Row>
      </Container>
    </section>
  );
}
