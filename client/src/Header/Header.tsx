import { MeganJohns } from "../types/MeganJohns";
import Title from "./Title";
import NavList from "./NavList";
import SocialBanner from "./SocialBanner/SocialBanner";
import { Container } from "react-bootstrap";

interface HeaderProps {
  mj: MeganJohns;
}

export default function Header(props: HeaderProps) {
  const mj = props.mj;
  return (
    <Container id="global-header" className="">
      <SocialBanner socials={mj.bio.social_urls} />
      <Title name={mj.bio.name} />
      <NavList />
    </Container>
  );
}
