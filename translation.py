from googletrans import Translator
from gtts import gTTS
import os


mytext = "You are beautiful"

translator = Translator()
result = translator.translate(mytext,dest='hi')
print(result.text)

language = 'hi'
myobj = gTTS(text=result.text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
