import { ListGroup } from "react-bootstrap";
import { ProfessionalService } from "../types/Bio";

interface ProfessionalServicesProps {
  services: ProfessionalService[];
}

export default function ProfessionalServices(props: ProfessionalServicesProps) {
  const services = props.services;
  return (
    <>
      <h4>Professional Services</h4>
      <ListGroup>
        {services.map((service) => (
          <ListGroup.Item>{service.service_name}</ListGroup.Item>
        ))}
      </ListGroup>
    </>
  );
}
