import os
import pathlib
from pathlib import Path
import feedgen
from feedgen.feed import FeedGenerator
from jinja2 import Environment, FileSystemLoader


def scandir():
    rss_paths = []
    for dirpath, dirnames, filenames in os.walk("audio"):
        if not dirnames: 
            # Found a leaf dir. See if it contains audio files!

            def is_audio_file(path):
                root, ext = os.path.splitext(path)
                if ext in [".mp3", ".ogg"]:
                    return True
                else:
                    return False

            audio_files = filter(is_audio_file, filenames)
            audio_files = list(audio_files)
            
            if len(audio_files) == 0:
                continue
            
            print(list(audio_files))

            # This directory has some audio files. Treat it as a single album,
            # and create an RSS feed for it!

            print(dirpath, "has 0 subdirectories and", len(filenames), "files")

            fg = FeedGenerator()
            fg.load_extension('podcast')
            fg.podcast.itunes_category('Technology', 'Podcasting')
            _, leafdir = os.path.split(dirpath)
            fg.title(f"{leafdir}")
            # fg.link(f"{leafdir}")
            fg.link( href='http://example.com', rel='alternate' )

            fg.description(f"{leafdir}")

            base_url = os.environ.get("POD2RSSD_BASE_URL") or f"http://localhost:8000"
            print("audio_files")
            for audio_file in audio_files:
                fe = fg.add_entry()
                file_srvpath = f"{base_url}/{dirpath}/{audio_file}"
                print("audio_file : ", file_srvpath)
                fe.id(file_srvpath)
                fe.title(audio_file)
                fe.description(audio_file)
                fe.enclosure(file_srvpath, 0, 'audio/mpeg')


            fg.rss_str(pretty=True)
            fg.rss_file(f"{dirpath}.xml")

            rss_srvpath = f"{base_url}/{dirpath}.xml"
            
            print(rss_srvpath)
            
            rss_paths.append({
                "name": dirpath,
                "url": rss_srvpath
            })
            
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("index.html.template")
    
    content = template.render(audiobooks=rss_paths)
    with open("audio/index.html", mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote index.html")

scandir()
