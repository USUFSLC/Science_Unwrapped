import pyaudio
import wave

# define stream chunk
chunk = 1024


# fake playC function for testing please delete this later
def playC():
    print("Playing C")


    #open a wav format music
    f = wave.open(r"WaveFiles\Music_Notes\C.wav", "rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()


# fake playD function for testing please delete this later
def playD():
    print("Playing D")

    # open a wav format music
    f = wave.open(r"WaveFiles\Music_Notes\D.wav", "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()


# fake touch functions for testing purposes, delete later
def getTouch0():
    return True


def getTouch1():
    return True
