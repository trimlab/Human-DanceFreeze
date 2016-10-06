import pyaudio
import wave

CHUNK = 1024

def playfile(file):
    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()