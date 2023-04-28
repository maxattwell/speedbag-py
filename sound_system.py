import sounddevice as sd
import soundfile as sf


def record_sound(duration):
    # record a sound for 10 seconds
    myrecording = sd.rec(int(duration * 48000), samplerate=48000, channels=2)
    sd.wait()
    return myrecording


def play_sound(recording):
    # play the recorded sound
    sd.play(recording, 48000)
    sd.wait()


def save_sound(recording, filename):
    # save the recorded sound
    sf.write(filename, recording, 48000)


# save_sound(record_sound(1), "test.wav")
