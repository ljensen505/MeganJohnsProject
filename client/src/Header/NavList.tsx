import { Col, Container, ListGroup, Row } from "react-bootstrap";
import "./Header.css";

export default function NavList() {
  return (
    <Container>
      <Row className="justify-content-center">
        <Col xs="auto">
          <ListGroup horizontal className="justify-content-center navbar-title">
            <ListGroup.Item>
              <a href="#discography">Music</a>
            </ListGroup.Item>
            <ListGroup.Item>
              <a href="#artwork">Art</a>
            </ListGroup.Item>
            <ListGroup.Item>
              <a href="#videos">Videos</a>
            </ListGroup.Item>
            <ListGroup.Item>
              <a href="#about">About</a>
            </ListGroup.Item>
            <ListGroup.Item disabled>News</ListGroup.Item>
          </ListGroup>
        </Col>
      </Row>
    </Container>
  );
}
