# weRecord
Wechat audio stitcher, takes a bundle of `.aud` wechat voice data and stitches them together to become one long `.mp3` file.

## dependencies
- Python 3
- ffmpeg
- mp3wrap
- make

## usage
- pull or download the files in this repository into an empty directory
- put all wechat voice data into a directory called `data` in the same directory as the scripts
- run `make`, the stitched together `.mp3` file will now appear on the same level as the scripts
