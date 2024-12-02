import "./Header.css";

interface TitleProps {
  name: string;
}

export default function Title(props: TitleProps) {
  return (
    <h2>
      <a href="#root" className="title navbar-title" id="title">
        {props.name}
      </a>
    </h2>
  );
}
