import os
import queue
import sounddevice as sd
import vosk

q = queue.Queue()

def ouvir_usuario():
    if not os.path.exists(r"C:\Users\Usuário\Documents\IA\Demeter\Demeter\models\reconhecimento_voz"):
        return "modelo vosk ausente"

    model = vosk.Model(r"C:\Users\Usuário\Documents\IA\Demeter\Demeter\models\reconhecimento_voz")
    samplerate = 16000

    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 Aguardando comando...")
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                import json
                texto = json.loads(result)["text"]
                return texto
