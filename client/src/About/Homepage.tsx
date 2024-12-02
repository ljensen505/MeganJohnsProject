import { Bio, ProfessionalService } from "../types/Bio";
import Quotes from "../Quotes/Quotes";
import { Quote } from "../types/Quote";
import ProfessionalServices from "./ProfessionalServices";

interface AboutProps {
  bio: Bio;
  quotes: Quote[];
  services: ProfessionalService[];
}

export default function About(props: AboutProps) {
  const bio = props.bio;
  const quotes = props.quotes;
  const services = props.services;
  const bioHTML = () => {
    return { __html: bio.bio };
  };

  return (
    <section id="about" className="content-section">
      <h2>Bio</h2>
      <div dangerouslySetInnerHTML={bioHTML()} />
      <ProfessionalServices services={services} />
      <Quotes quotes={quotes} />
    </section>
  );
}
