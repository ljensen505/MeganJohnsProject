import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import About from "./About/Homepage";
import { getMeganJohns } from "./Api";
import "./App.css";
import Header from "./Header/Header";
import MjSection from "./MjSection";
import Reel from "./Reel/Reel";
import type { Album } from "./types/Album";
import type { Artwork } from "./types/Artwork";
import type { Bio, ProfessionalService } from "./types/Bio";
import type { MeganJohns } from "./types/MeganJohns";
import type { Quote } from "./types/Quote";
import type { Video } from "./types/Video";
import Videos from "./Videos/Videos";

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
      },
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
        <Reel />
        <MjSection sectionTitle="discography" works={albums} />
        <MjSection sectionTitle="artwork" works={artwork} />
        <Videos videos={videos} />
        <About bio={bio} quotes={quotes} services={services} />
      </Container>
    </Container>
  );
}

export default App;
