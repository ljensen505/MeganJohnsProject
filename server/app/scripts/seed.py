from pathlib import Path

from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from app.constants import (
    ALBUMS_TABLE,
    ART_MEDIUM_TABLE,
    ARTICLES_TABLE,
    ARTISTS_TABLE,
    ARTWORK_TABLE,
    BIO_CONTENT_TABLE,
    QUOTES_TABLE,
    SERVICES_TABLE,
    SOCIAL_TABLE,
    VIDEOS_TABLE,
)
from app.db.conn import connect_db
from app.model import Album, Artist, Artwork, Medium, Quote, Video
from app.model.articles import Article
from app.model.bio import Bio, ProfessionalService, SocialUrl

# videos
videos: list[Video] = [
    Video(
        title="Human",
        subtitle="(Official Music Video)",
        description="<p>Song and Video Written, Performed, Produced, Recorded, Filmed and Edited by Megan Johns.</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/HiskLzZHX48?si=yomwnyr4FkupXU1e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://youtu.be/HiskLzZHX48?si=WA30xIpf1iSfJvPt",  # type: ignore
    ),
    Video(
        title="EQUALITY IS HERE".title(),
        subtitle="(Dark Comedy)",
        description="<p>Song by Megan Johns Video Written, Directed, Produced, Storyboarded, and Edited by Megan Johns</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/TvXPCKv7eg4?si=AOrnPvhDS1NMD0tQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://youtu.be/TvXPCKv7eg4?si=kpUFyN3TM-FjJ67B",  # type: ignore
    ),
    Video(
        title="Feathers",
        subtitle="(34 Minute Dark Fantasy Drama)",
        description="<p>Written, Directed, Produced, Storyboarded, Co-Scored and Co-Edited by Megan Johns Starring Sara Blythe Visual Effects by Dylan Keim Produced by MoonWish Productions, Tendrile Productions, BluryFilms, One Tree Productions LLC, and Oros Productions Director of Photography Walter King Score by Megan Johns and Shannon Swords (Bubble Bubble Gum Gum)</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/tk8LlaAwgCg?si=olWVWRrhVEVxhFKp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://youtu.be/tk8LlaAwgCg?si=hvREJdL6DZ3CkySb",  # type: ignore
        website="https://feathersmovie.weebly.com/",  # type: ignore
    ),
    Video(
        title="Gemini",
        subtitle="(Official Music Video) (From 2019 Movie 'Live Free Or Die')",
        description="<p>Song Written by Megan Johns Video Directed by Chelsea Real Video Edited by Megan Johns (MoonWish Productions) and One Tree Productions LLC</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/pWCTmCl9Im4?si=CORUdH3m5SS57nmU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://www.youtube.com/watch?v=pWCTmCl9Im4",  # type: ignore
    ),
    Video(
        title="Talk of Dreams",
        subtitle="(Official Music Video)",
        description="<p>Video Directed and Edited by Rick Gates (Tendrile Productions) Camera Operated by Rick Gates, James Kaiser, and Nick Pemble</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/yhXF5F_4F_k?si=o3kdxe9cRQXoHH0Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://youtu.be/yhXF5F_4F_k?si=MIi0uMHhg1kTYDYe",  # type: ignore
    ),
    Video(
        title="Still",
        subtitle="(Official Music Video)",
        description="<p>Song Written by Megan Johns Video Directed and Edited by Matt HarsH & Sam Ambler Director of Photography Mark Spomer</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/USNr1pJRXR4?si=DpHG_wR6BGaNlT3o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://www.youtube.com/watch?v=USNr1pJRXR4",  # type: ignore
    ),
    Video(
        title="By the Way",
        subtitle="(EFS 72 Hr Music Video Contest Entry)",
        description="<p>Song Written by Megan Johns Video Written, Directed and Edited Whitney Peterson Filmed by Whitney Peterson & Cody Van Roberts</p>",
        embedded_player_iframe="""<iframe src="https://player.vimeo.com/video/167692299?h=40de8a4ade" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>""",
        source="https://www.youtube.com/watch?v=RFad185zIYw",  # type: ignore
    ),
    Video(
        title="Sunday Drive",
        subtitle="(Official Music Video)",
        description="<p>Song Written by Megan Johns Video Directed, Filmed and Edited by Garrick Nelson</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/cX8K4BJbWWg?si=vSE8HNVJbBH54YQL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://www.youtube.com/watch?v=cX8K4BJbWWg",  # type: ignore
    ),
    Video(
        title="Hey, Lonely",
        subtitle="(Official Music Video)",
        description="<p>Song Written by Megan Johns Video Directed, Filmed and Edited by James Triechler</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/AmrUTugnP2s?si=9XRy3D7hi7GHq_qV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://youtu.be/AmrUTugnP2s?si=sGPhNkYynj2iyPnt",  # type: ignore
    ),
    Video(
        title="Moonwish - Gemini",
        subtitle="(Electronic Version)",
        description="<p>Song Written by Megan Johns</p><p>Video Directed, Filmed and Edited by John Isberg</p><p>Video Produced by Matt HarsH, John Isberg and Megan Johns</p>",
        embedded_player_iframe="""<iframe src="https://player.vimeo.com/video/143818518?h=2159fc0374" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>""",
        source="https://vimeo.com/143818518?embedded=true&source=vimeo_logo&owner=31047464",  # type: ignore
    ),
    Video(
        title="CAFÉ Song".title(),
        subtitle="(Official Music Video)",
        description="<p>Song Written, Performed, and Produced by Megan Johns Video Directed, Filmed and Edited by Matt HarsH</p>",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/llp2oi3zb_8?si=LrgxWYwmbHgBi_Es" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://www.youtube.com/watch?v=llp2oi3zb_8&t=10s",  # type: ignore
    ),
    Video(
        title="THE BEAT WAS BURNT".title(),
        subtitle="(Official Music Video)",
        description="Song Written by Megan Johns Video Directed by Matt HarsH and Filmed by Sam Ambler",
        embedded_player_iframe="""<iframe width="560" height="315" src="https://www.youtube.com/embed/5fDfH7XD92s?si=hULHJgCfe_iRrdiS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
        source="https://www.youtube.com/watch?v=5fDfH7XD92s",  # type: ignore
    ),
]

# quotes
quotes = [
    Quote(
        body="Something like Trent Reznor taking over the Smashing Pumpkins and replacing Corgan with Tori Amos.",
        author="Middle Tennessee Music",
        source="https://www.indiemusicdiscovery.com/megan-johns-says-hey-lonely/",  # type: ignore
    ),
    Quote(
        body="Melodic and hypnotizing. | Best Local Singer-Songwriter 2013",
        author="Smile Politely",
        source="http://www.smilepolitely.com/music/best_music_2013/",  # type: ignore
    ),
    Quote(
        body="Tight aggressive power chords underpin Johns's raspy yet melodic singing voice, telling a story in impressionistic fragments rather than a single narrative.",
        author="Eugene Magazine",
    ),
    Quote(
        body="Johns creates music that is at once sweet and biting: the languid tone of her voice providing a perfect lace overlay to the harder-rocking arrangements beneath them.",
        author="The News Gazette",
    ),
    Quote(
        body="She lures her listeners to unearth a deeper subconscious level.",
        author="The Buzz Weekly",
    ),
]

# Social & Bio information
socials = [
    SocialUrl(
        social_name="itunes",
        social_url="https://itunes.apple.com/us/artist/megan-johns/74351585",  # type: ignore
    ),
    SocialUrl(
        social_name="facebook",
        social_url="http://www.facebook.com/meganjohnsmusic",  # type: ignore
    ),
    SocialUrl(
        social_name="soundcloud",
        social_url="https://soundcloud.com/meganjohns",  # type: ignore
    ),
    SocialUrl(
        social_name="youtube",
        social_url="http://youtube.com/user/MeganJohnsVideos",  # type: ignore
    ),
    SocialUrl(
        social_name="instagram",
        social_url="https://instagram.com/meganjohnsmusic/",  # type: ignore
    ),
    SocialUrl(
        social_name="spotify",
        social_url="https://open.spotify.com/artist/3CTUWD06ndDSuuUUJHm1bf",  # type: ignore
    ),
    SocialUrl(
        social_name="bandcamp",
        social_url="https://meganjohns.bandcamp.com/track/i-am-old",  # type: ignore
    ),
]

services = [
    ProfessionalService(service_name="Music Composition & Performance"),
    ProfessionalService(service_name="Audio Engineering"),
    ProfessionalService(service_name="Voice Over & Acting"),
    ProfessionalService(service_name="Videography / Filmmaking"),
    ProfessionalService(service_name="Visual Art"),
    ProfessionalService(service_name="Classes"),
]


bio_html_content = ""

ROOT_DIR = Path(__file__).parent
HTML_FILE = ROOT_DIR / "bio.html"
with open(HTML_FILE, "r") as html_file:
    for line in html_file.readlines():
        bio_html_content += line.strip()

bio = Bio(name="Megan Johns", bio=bio_html_content, social_urls=socials)

# art mediums
arcylic = Medium(medium_name="Acrylic on Canvas")
oil = Medium(medium_name="Oil on Canvas")
zinc = Medium(medium_name="Zinc Plate Etching")
charcol = Medium(medium_name="Charcol on Paper")
rice_paper = Medium(medium_name="Pen and Ink on Rice Paper")
watercolor = Medium(medium_name="Watercolor on Paper En Plein Air")
illustrator_poster = Medium(medium_name="Illustrator Poster")
graphic_design = Medium(medium_name="Graphic Design")

mediums = [
    arcylic,
    oil,
    zinc,
    charcol,
    rice_paper,
    watercolor,
    illustrator_poster,
    graphic_design,
]

# artwork
# https://docs.google.com/spreadsheets/d/1RMAGgpEAjEL6Kf-QGTKxuZXZD5Cqy7NVG2pnAPctcdw/edit?gid=0#gid=0
artwork: list[Artwork] = [
    Artwork(
        artwork_name="Gas Mask Study",
        medium=oil,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1721007132/MeganJohns/Art/Gaslit_Megan_Johns__Acrylic_on_Canvas_2009_ccge5s.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010768/MeganJohns/Art/thumbnails/Gaslit_Megan_Johns__Acrylic_on_Canvas_2009_ccge5s-400x311_aplzhd.jpg",  # type: ignore
        release_year=2009,
        size='11"x14"',
    ),
    Artwork(
        artwork_name="Women's March",
        is_featured=True,
        medium=arcylic,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1720988650/MeganJohns/Art/Women_s_March_Painting_24x36_Acrylic_on_Canvas_2017_Megan_Johns_dct1vp.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010773/MeganJohns/Art/thumbnails/Women_s_March_Painting_24x36_Acrylic_on_Canvas_2017_Megan_Johns_dct1vp-400x264_i3p4mx.jpg",  # type: ignore
        release_year=2017,
        size='24"x36"',
    ),
    Artwork(
        artwork_name="Spilled Beans Study",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1720992412/MeganJohns/Art/Spilled_Beans_Signature_2019_q81yvi.png",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010768/MeganJohns/Art/thumbnails/Spilled_Beans_Signature_2019_q81yvi-400x400_daovzb.png",  # type: ignore
        release_year=2019,
    ),
    Artwork(
        artwork_name="Captain",
        medium=zinc,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718391476/MeganJohns/Art/Captain_9x12_Zinc_Plate_Etching_2009_zxh2wm.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010768/MeganJohns/Art/thumbnails/Captain_9x12_Zinc_Plate_Etching_2009_zxh2wm-400x267_few8in.jpg",  # type: ignore
        release_year=2009,
        size='9"x12"',
    ),
    Artwork(
        artwork_name="Resting Chill Face",
        medium=arcylic,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1720992884/MeganJohns/Art/Resting_Chill_Face_16x20_Acrylic_on_Canvas_from_Life_2019_edited_no_edges_hfw28u.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010772/MeganJohns/Art/thumbnails/Resting_Chill_Face_16x20_Acrylic_on_Canvas_from_Life_2019_edited_no_edges_hfw28u-316x400_umgpus.jpg",  # type: ignore
        release_year=2019,
        size='16"x12"',
    ),
    Artwork(
        artwork_name="Louis XIV",
        medium=arcylic,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1720988576/MeganJohns/Art/Louis_XIV_16x20_Acrylic_on_Canvas_2019_Megan_Johns_kmbirh.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010769/MeganJohns/Art/thumbnails/Louis_XIV_16x20_Acrylic_on_Canvas_2019_Megan_Johns_kmbirh-319x400_ixelam.jpg",  # type: ignore
        release_year=2019,
        size='16"x20"',
    ),
    Artwork(
        artwork_name="Allerton",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1720988504/MeganJohns/Art/Allerton_FU_Dog_Watercolor_on_Paper_En_Plein_Air_no_edges_cmkbjs.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010771/MeganJohns/Art/thumbnails/Allerton_FU_Dog_Watercolor_on_Paper_En_Plein_Air_no_edges_cmkbjs-300x400_odzydz.jpg",  # type: ignore
    ),
    Artwork(
        artwork_name="Goat and Rooster",
        medium=arcylic,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1720988474/MeganJohns/Art/Goat_and_Rooster_16x20_Acrylic_on_Canvas_2019_Np_edges_d2y7hk.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010771/MeganJohns/Art/thumbnails/Goat_and_Rooster_16x20_Acrylic_on_Canvas_2019_Np_edges_d2y7hk-314x400_uhskcy.jpg",  # type: ignore
        release_year=2019,
        size='16"x20"',
    ),
    Artwork(
        artwork_name="Feathers Poster",
        medium=graphic_design,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718413105/MeganJohns/Art/Feathers_Poster_Graphic%20Design_2020_hcjej2.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010771/MeganJohns/Art/thumbnails/Feathers_Poster_Graphic_20Design_2020_hcjej2-270x400_zwzwd3.jpg",  # type: ignore
        release_year=2020,
    ),
    Artwork(
        artwork_name="Hey Lonely",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718391586/MeganJohns/Art/Hey_Lonely_Photoshopped_Photography_2012_h1aitf.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010773/MeganJohns/Art/thumbnails/Hey_Lonely_Photoshopped_Photography_2012_h1aitf-400x400_l0bghw.jpg",  # type: ignore
        release_year=2012,
    ),
    Artwork(
        artwork_name="Teapot and Teacup",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718391538/MeganJohns/Art/Teapot_and_Teacup_Acrylic_on_Canvas_2017_r6ivpo.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010769/MeganJohns/Art/thumbnails/Teapot_and_Teacup_Acrylic_on_Canvas_2017_r6ivpo-400x233_ztsjtv.jpg",  # type: ignore
        release_year=2017,
    ),
    Artwork(
        artwork_name="Polyphemus Moth",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718391523/MeganJohns/Art/Polyphemus_Moth_16x16_Acrylic_on_Canvas_Megan_Johns_hgqc1h.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010771/MeganJohns/Art/thumbnails/Polyphemus_Moth_16x16_Acrylic_on_Canvas_Megan_Johns_hgqc1h-400x400_vlnju2.jpg",  # type: ignore
        size='16"x16"',
    ),
    Artwork(
        artwork_name="Lou",
        medium=arcylic,
        release_year=2019,
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718391496/MeganJohns/Art/Lou_Acrylic_on_Canvas_2019_fze7qc.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010769/MeganJohns/Art/thumbnails/Lou_Acrylic_on_Canvas_2019_fze7qc-320x400_cf5ed9.jpg",  # type: ignore
    ),
    Artwork(
        artwork_name="Silver Teapot",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718349058/MeganJohns/Art/Silver_Teapot_12x12_Acrylic_on_Canvas_2017_Megan_Johns_zfrknd.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010771/MeganJohns/Art/thumbnails/Silver_Teapot_12x12_Acrylic_on_Canvas_2017_Megan_Johns_zfrknd-400x400_tz6ovb.jpg",  # type: ignore
        release_year=2017,
        size='12"x12"',
    ),
    Artwork(
        artwork_name="Gemini",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718347980/MeganJohns/Art/Gemini_Single_Album_Cover_Photoshoped_Photography__2015_Megan_Johns_v4zwao.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010769/MeganJohns/Art/thumbnails/Gemini_Single_Album_Cover_Photoshoped_Photography__2015_Megan_Johns_v4zwao-400x400_a7kgs5.jpg",  # type: ignore
        release_year=2015,
    ),
    Artwork(
        artwork_name="Glass Ceiling",
        source="https://res.cloudinary.com/dreftv0ue/image/upload/v1718347979/MeganJohns/Art/Glass_Cieling_Self_Portrait_Acrylic_on_Canvas_2009_Megan_Johns_jsgupl.jpg",  # type: ignore
        thumbnail="https://res.cloudinary.com/dreftv0ue/image/upload/v1721010769/MeganJohns/Art/thumbnails/Glass_Cieling_Self_Portrait_Acrylic_on_Canvas_2009_Megan_Johns_jsgupl-400x269_luwr5i.jpg",  # type: ignore
        release_year=2009,
    ),
]

# news articles
# TODO
articles: list[Article] = []

# album artists
megan_artist = Artist(
    artist_name="Megan Johns",
    artist_url="https://music.apple.com/us/artist/megan-johns/74351585",  # type: ignore
)
greytones = Artist(
    artist_name="The Greytones",
    artist_url="https://open.spotify.com/artist/5JyA3JrRMinqhLslj7EyLl",  # type: ignore
)
bubble_bubble_bum_bum = Artist(
    artist_name="Bubble Bubble Gum Gum",
    artist_url="https://music.apple.com/us/artist/bubble-bubble-gum-gum/1554007615",  # type: ignore
)
artists: list[Artist] = [megan_artist, greytones, bubble_bubble_bum_bum]

# discography
albums: list[Album] = [
    Album(
        album_name="Dirty Shoes",
        release_year=2005,
        artist=megan_artist,
        apple_music_url="https://music.apple.com/us/album/dirty-shoes/74351635",  # type: ignore
        bandcamp_url="https://meganjohns.bandcamp.com/track/fog",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363942/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Dirty_Shoes_Cover_2005_bnb8u0.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=2275072448/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/fog">Fog by Megan Johns</a></iframe>',
    ),
    Album(
        album_name="Hey, Lonely",
        release_year=2012,
        artist=megan_artist,
        apple_music_url="https://music.apple.com/us/album/hey-lonely/565637660",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363966/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Hey_Lonely_Jacket_hires-2_kwo34f.jpg",  # type: ignore
        rear_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717364028/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Hey_Lonely_Reverse2_esmjia.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=2623205502/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/album/hey-lonely">Hey, Lonely by Megan Johns</a></iframe>',
    ),
    Album(
        album_name="Gemini",
        release_year=2015,
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/gemini",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363956/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Gemini_MoonWish_Single_2015_spgv2m.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=2493215358/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/gemini">Gemini by Moonwish</a></iframe>',
    ),
    Album(
        album_name="Inner Voice",
        release_year=2019,
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/album/inner-voice-ep",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363981/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Inner_Voice_EP_2019_po0nbq.jpg",  # type: ignore
        rear_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363984/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Inner_Voice_EP_Backcover_2019_ilenfq.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=1645073059/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/album/inner-voice-ep">Inner Voice EP by Megan Johns</a></iframe>',
    ),
    Album(
        album_name="MoonWish Recordings 2015",
        release_year=2015,
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/album/moonwish-recordings-2015",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363988/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/MoonWish_Recordings_2015_j3pzyd.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=3211709152/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/album/moonwish-recordings-2015">MoonWish Recordings 2015 by Megan Johns</a></iframe>',
    ),
    Album(
        album_name="Penumbra",
        release_year=2007,
        artist=greytones,
        spotify_url="https://open.spotify.com/album/1FMhRBPjhCOe21JNwgYUAb",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363997/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/The_Greytones_Penumbra_Cover_2007_rh02wu.jpg",  # type: ignore
    ),
    Album(
        album_name="Feathers",
        release_year=2021,
        artist=bubble_bubble_bum_bum,
        spotify_url="https://music.apple.com/us/album/feathers-original-motion-picture-score/1554024529",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363949/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Feathers_Score_Bubble_Bubble_Gum_Gum_2021_itjio0.jpg",  # type: ignore
    ),
    Album(
        album_name="Human",
        release_year=2022,
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/human",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363973/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Human_Single_2022_lknlpc.png",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=3620590740/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/human">Human by Megan Johns</a></iframe>',
    ),
    Album(
        album_name="I Am Old",
        release_year=2022,
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/i-am-old",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363976/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/I_Am_Old_Single_2022_mao2yw.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=2078638263/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/i-am-old">I Am Old by Megan Johns</a></iframe>',
    ),
]


def get_db_cursor() -> tuple[MySQLConnection, MySQLCursor]:
    db = connect_db()
    cursor = db.cursor()
    return db, cursor


def close_db_cursor(db: MySQLConnection, cursor: MySQLCursor) -> None:
    db.commit()
    cursor.close()
    db.close()


def drop_tables():
    db, cursor = get_db_cursor()
    for table in [
        ALBUMS_TABLE,
        ARTISTS_TABLE,
        ARTICLES_TABLE,
        ARTWORK_TABLE,
        ART_MEDIUM_TABLE,
        BIO_CONTENT_TABLE,
        SOCIAL_TABLE,
        QUOTES_TABLE,
        VIDEOS_TABLE,
        SERVICES_TABLE,
    ]:
        print(f"dropping table: {table}")
        cursor.execute(
            f"""-- sql
        DROP TABLE IF EXISTS {table};
        """
        )
    close_db_cursor(db, cursor)
    print("")


def seed_albums() -> None:
    print(f"seeding {len(albums)} albums")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {ALBUMS_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            album_name VARCHAR(255) NOT NULL,
            release_year YEAR,
            artist_id INT,
            spotify_url VARCHAR(255),
            itunes_url VARCHAR(255),
            bandcamp_url VARCHAR(255),
            apple_music_url VARCHAR(255),
            front_artwork_url VARCHAR(255),
            rear_artwork_url VARCHAR(255),
            bandcamp_player VARCHAR(1024),
            PRIMARY KEY (id),
            FOREIGN KEY (artist_id) REFERENCES {ARTISTS_TABLE}(id) ON DELETE CASCADE
        );
        """
    )
    for album in albums:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ALBUMS_TABLE} (album_name, release_year, artist_id, spotify_url, itunes_url, bandcamp_url, apple_music_url, front_artwork_url, rear_artwork_url, bandcamp_player)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                album.album_name,
                album.release_year,
                album.artist.id,
                str(album.spotify_url) if album.spotify_url else None,
                str(album.itunes_url) if album.itunes_url else None,
                str(album.bandcamp_url) if album.bandcamp_url else None,
                str(album.apple_music_url) if album.apple_music_url else None,
                str(album.front_artwork_url) if album.front_artwork_url else None,
                str(album.rear_artwork_url) if album.rear_artwork_url else None,
                album.bandcamp_player,
            ),
        )
        if cursor.lastrowid:
            album.id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()


def seed_quotes() -> None:
    print(f"seeding {len(quotes)} quotes")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {QUOTES_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            body VARCHAR(1000) NOT NULL,
            author VARCHAR(255) NOT NULL,
            source VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )
    for quote in quotes:
        cursor.execute(
            f"""-- sql
            INSERT INTO {QUOTES_TABLE} (body, author, source)
            VALUES (%s, %s, %s);
            """,
            (quote.body, quote.author, str(quote.source) if quote.source else None),
        )
        if cursor.lastrowid:
            quote.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_artists() -> None:
    print(f"seeding {len(artists)} artists")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {ARTISTS_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            artist_name VARCHAR(255) NOT NULL,
            artist_url VARCHAR(255) NOT NULL,
            PRIMARY KEY (id)
        );
        """
    )
    for artist in artists:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ARTISTS_TABLE} (artist_name, artist_url)
            VALUES (%s, %s);
            """,
            (artist.artist_name, str(artist.artist_url)),
        )
        if cursor.lastrowid:
            artist.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_articles():
    print(f"seeding {len(articles)} articles")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE articles (
            id INT NOT NULL AUTO_INCREMENT,
            article_title VARCHAR(255) NOT NULL,
            body VARCHAR(255) NOT NULL,
            video_url VARCHAR(255),
            is_featured BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (id)
        );
        """
    )
    for article in articles:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ARTICLES_TABLE} (article_title, body, video_url, is_featured)
            VALUES (%s, %s, %s, %s)
            """,
            (
                article.article_title,
                article.body,
                str(article.video_url),
                article.is_featured,
            ),
        )
        if cursor.lastrowid:
            article.id = cursor.lastrowid

    db.commit()
    cursor.close()
    db.close()


def seed_artwork():
    print(f"seeding {len(artwork)} pieces of art")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {ARTWORK_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            medium_id INT,
            artwork_name VARCHAR(255) UNIQUE NOT NULL,
            source VARCHAR(255) NOT NULL,
            thumbnail VARCHAR(255) NOT NULL,
            is_featured BOOLEAN DEFAULT FALSE,
            release_year YEAR,
            size VARCHAR(255),
            PRIMARY KEY (id),
            FOREIGN KEY (medium_id) REFERENCES {ART_MEDIUM_TABLE}(id) ON DELETE CASCADE
        );
        """
    )
    for work in artwork:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ARTWORK_TABLE} (medium_id, artwork_name, source, thumbnail, is_featured, release_year, size)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """,
            (
                work.medium.id if work.medium is not None else None,
                work.artwork_name,
                str(work.source),
                str(work.thumbnail),
                work.is_featured,
                work.release_year,
                work.size,
            ),
        )
        if cursor.lastrowid:
            work.id = cursor.lastrowid

    close_db_cursor(db, cursor)


def seed_mediums():
    print(f"seeding {len(mediums)} art mediums")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {ART_MEDIUM_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            medium_name VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )
    for medium in mediums:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ART_MEDIUM_TABLE} (medium_name)
            VALUES (%s);
            """,
            (medium.medium_name,),
        )
        if cursor.lastrowid:
            medium.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_social_info():
    print(f"seeding {len(socials)} social urls")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {SOCIAL_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            social_name VARCHAR(255) NOT NULL UNIQUE,
            social_url VARCHAR(255) NOT NULL UNIQUE,
            primary key (id)
        );
        """
    )
    for s in socials:
        cursor.execute(
            f"""-- sql
            INSERT INTO {SOCIAL_TABLE} (social_name, social_url)
            VALUES (%s, %s);
            """,
            (s.social_name, str(s.social_url)),
        )
        if cursor.lastrowid:
            s.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_professional_services():
    print(f"seeding {len(services)} professional services")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {SERVICES_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            service_name VARCHAR(255) NOT NULL UNIQUE,
            primary key (id)
        );
        """
    )
    for s in services:
        cursor.execute(
            f"""-- sql
            INSERT INTO {SERVICES_TABLE} (service_name)
            VALUES (%s);
            """,
            (s.service_name,),
        )
        if cursor.lastrowid:
            s.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_bio():
    print(f"seeding single bio")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {BIO_CONTENT_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            content TEXT NOT NULL,
            primary key (id)
        );
        """
    )
    cursor.execute(
        f"""-- sql
        INSERT INTO {BIO_CONTENT_TABLE} (content)
        VALUES (%s);
        """,
        (bio.bio,),
    )
    close_db_cursor(db, cursor)


def seed_videos() -> None:
    print(f"seeding single bio")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {VIDEOS_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            title VARCHAR(255) NOT NULL,
            subtitle VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            source VARCHAR(255) NOT NULL,
            embedded_player_iframe TEXT,
            website VARCHAR(255),
            primary key (id)
        );
        """
    )
    for video in videos:
        cursor.execute(
            f"""-- sql
            INSERT INTO {VIDEOS_TABLE} (title, subtitle, description, source, embedded_player_iframe, website)
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            (
                video.title,
                video.subtitle,
                video.description,
                str(video.source),
                video.embedded_player_iframe,
                str(video.website) if video.website else None,
            ),
        )
        if cursor.lastrowid:
            video.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def main() -> None:
    drop_tables()
    seed_artists()
    seed_albums()
    seed_articles()
    seed_mediums()
    seed_artwork()
    seed_social_info()
    seed_bio()
    seed_quotes()
    seed_videos()
    seed_professional_services()
