import { Figure } from "react-bootstrap";
import "./Quotes.css";

interface QuoteProps {
  body: string;
  author: string;
  source_url?: string;
}

export default function QuoteElement(props: QuoteProps) {
  return (
    <Figure>
      <blockquote>
        <p className="quote-body">{props.body}</p>
        <figcaption className="blockquote-footer quote-giver">
          {props.author}
        </figcaption>
      </blockquote>
    </Figure>
  );
}
