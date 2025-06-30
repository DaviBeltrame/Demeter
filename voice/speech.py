from gtts import gTTS
import pygame
import os 

def falar(texto):
    print(f"Deméter: {texto}")
    tts = gTTS(text=texto, lang='pt')
    tts.save("fala.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("fala.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue    
    pygame.mixer.music.unload()
    os.remove("fala.mp3")
