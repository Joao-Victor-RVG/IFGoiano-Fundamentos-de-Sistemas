from gtts import gTTS
from playsound import playsound

audio = 'meusom.mp3'
idioma = 'fr'
conversao = gTTS(
    text = 'teste',
    lang = idioma
)

conversao.save(audio)



