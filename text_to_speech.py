from gtts import gTTS
from playsound import playsound
import datetime

text = "Glory be to the Father, and to the Son, and to the Holy Spirit, as it was in the beginning, is now, and ever shall be, world without end. Amen!"
language = "en"
now=datetime.datetime.now()
# fn=now.strftime("C:/Users/HP/gTTS_audio_files/%Y_%m_%d_%H_%M_%S.mp3")

# resultobj = gTTS(text=text, lang=language, slow=False)

# resultobj.save(fn)
# playsound(fn)