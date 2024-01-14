# pod2rssd
Simple python server to automatically generate RSS feeds (for podcasts/audiobooks) from a nested directory of audio content, which it also serves.

For each leaf subdirectory under 'audio':
 - Enumerate each audio file within that subdirectory
 - Generate the RSS feed containing each audio file as an entry
 - Save it as 'audio/subdir/[...]/subdir2.xml
  
Serve at:
https://{base_url}/audio/subdir/subdir2/file.mp3
https://{base_url}/audio/subdir/subdir2.xml
https://{base_url}/index.html
https://{base_url}/rescan.html