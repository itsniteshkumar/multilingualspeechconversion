import speech_recognition as sr
import webbrowser as wb
from googletrans import Translator
from gtts import gTTS
import os


r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print('Speak now')
    audio = r3.listen(source)
if 'hi' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    #while(1):
    with sr.Microphone() as source:
        #print('search your query: ')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            if 'exit' in get:
                exit(0)
            print(get)
            # wb.get().open_new(url+get)

        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

mytext = get

translator = Translator()
result = translator.translate(mytext,dest='hi')
print(result.text)

language = 'hi'
myobj = gTTS(text=result.text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
