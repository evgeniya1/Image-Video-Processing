import sounddevice
from scipy.io.wavfile import write

seconds = 5
fps = 44100

myrecording = sounddevice.rec(frames=seconds*fps, samplerate=fps,channels=1)
sounddevice.wait()
write('record_comp_audio.mp3', fps, myrecording)