import librosa
import time
import matplotlib.pyplot as plt
import sound_system as ss
import sound as sd

filename = "recording.wav"
countdown_file = "mixkit-start-match-countdown-1954.wav"
y, sr = librosa.load(countdown_file)
countdown_length = librosa.get_duration(y=y, sr=sr)
stop_file = "mixkit-appliance-ready-beep-1076.wav"
# get user input
duration = float(input("Enter duration in seconds: "))
print("Duration entered:", duration, "seconds")
sd.play_sound(countdown_file)
time.sleep(countdown_length)
print("start recording")
recording = ss.record_sound(duration)
ss.save_sound(recording, filename)
print("finish recording")
sd.play_sound(stop_file)

y, sr = librosa.load(filename)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

rms = librosa.feature.rms(y=y)

onset_env = librosa.onset.onset_strength(y=y, sr=sr, n_fft=2048)

# detect the onset frames
onset_frames = librosa.onset.onset_detect(
    onset_envelope=onset_env,
    y=rms,
    sr=sr,
    hop_length=256,
    backtrack=False,
    units="frames",
)

print(len(onset_frames) / 3)

plt.figure()
plt.plot(onset_env, label="Onset Strength")
plt.vlines(
    onset_frames,
    ymin=0,
    ymax=max(onset_env),
    color="r",
    linestyle="--",
    label="Onsets",
)
plt.xlabel("Frame")
plt.ylabel("Onset Strength")
plt.legend()
plt.show()
