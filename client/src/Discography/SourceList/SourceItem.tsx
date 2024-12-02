import { ListGroup } from "react-bootstrap";

interface SourceItemProps {
  sourceName: string;
  sourceUrl: string;
}

export default function SourceItem(props: SourceItemProps) {
  return (
    <ListGroup.Item>
      <a href={props.sourceUrl} target="_blank">
        {props.sourceName}
      </a>
    </ListGroup.Item>
  );
}
