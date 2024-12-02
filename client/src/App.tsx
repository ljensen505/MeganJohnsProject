import { useEffect, useState } from "react";
import { getMeganJohns } from "./Api";
import type { MeganJohns } from "./types/MeganJohns";
import type { Album } from "./types/Album";
import type { Artwork } from "./types/Artwork";
import type { Quote } from "./types/Quote";
import type { Video } from "./types/Video";
import type { Bio, ProfessionalService } from "./types/Bio";
import MjSection from "./MjSection";
import Header from "./Header/Header";
import About from "./About/Homepage";
import { Container } from "react-bootstrap";
import Videos from "./Videos/Videos";
import "./App.css";

function App() {
  const [mj, setMj] = useState<MeganJohns | undefined>(undefined);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [artwork, setArtwork] = useState<Artwork[]>([]);
  const [bio, setBio] = useState<Bio | undefined>(undefined);
  const [quotes, setQuotes] = useState<Quote[]>([]);
  const [videos, setVideos] = useState<Video[]>([]);
  const [services, setServices] = useState<ProfessionalService[]>([]);

  useEffect(() => {
    getMeganJohns().then(
      (mjData) => {
        setMj(mjData);
      },
      (error) => {
        console.error(error);
      }
    );
  }, []);

  useEffect(() => {
    if (mj) {
      setAlbums(mj.albums);
      setArtwork(mj.artwork);
      setBio(mj.bio);
      setQuotes(mj.quotes);
      setVideos(mj.videos);
      setServices(mj.professional_services);
    }
  }, [mj]);

  if (!mj || !bio) {
    return <>Loading</>;
  }

  return (
    <Container className="">
      <Container id="main-content">
        <Header mj={mj} />
        <MjSection sectionTitle="discography" works={albums} />
        <MjSection sectionTitle="artwork" works={artwork} />
        <Videos videos={videos} />
        <About bio={bio} quotes={quotes} services={services} />
      </Container>
    </Container>
  );
}

export default App;
