### Introduction

Text-To-Speech is a small project that enables users to test out and download speech derived from text. Features include:

- The ability to enter a custom message a user wants the program to say
- The ability to change the programs speech rate, volume, and gender
- The option to save the TTS into a .mp3 file
- All packaged into a neat and straightforward GUI interface

---

### How to Use YT Video Downloader

Using this app is super simple; as easy as 1, 2, 3! 

First, you need to type the actual message you want the program to read in the text box towards the left

Then, you need to select the volume, speech rate, and voice. Remember that the lower the speech rate, the slower the voice and vice-versa. 200 is recommended.

Lastly, you need to press the big button that says listen to listen to the program, then press download to download the file into the program's parent directory!

---

### Dependencies

This project only has 2 dependencies; the rest are native to Python:

- PyQt5 and its dependencies (`pip install PyQt5`)
- pyttsx3  (`pip install pyttsx3`)

If you are running this script on a Linux Distro, please make sure you have `espeak` and `ffmeg` installed, as shown below:
`sudo apt update && sudo apt install espeak ffmpeg libespeak1`

---

### Future Updates

At this moment no future updates are being considered.

---

**[Notion](https://ehtesham-ali.notion.site/Text-To-Speech-GUI-e8f03601dea04ffd90a2901496c18358) | [Website](https://ali-ehtesham.carrd.co/)**
