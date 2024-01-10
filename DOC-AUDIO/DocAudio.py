import docx2txt
from gtts import gTTS
import os

# Read the docx file
doc_path = '/Users/abbassyed/Documents/Assignments/DocAudio.docx'
text = docx2txt.process(doc_path)

# Print the text
print(text)

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save the spoken text to an audio file
tts.save("story.mp3")

# Play the audio file using the default system player
os.system("start story.mp3")