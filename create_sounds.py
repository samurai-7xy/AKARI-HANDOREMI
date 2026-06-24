import numpy as np
import wave
import struct

# 一回再生すると「ドレミ」のwavファイルができる
fs = 44100
a = 1.0

TONES = {
    'C4': 261.626,
    'D4': 293.665,
    'E4': 329.628
}

def create_wav(filename, freq, sec=0.5):

    n = np.arange(fs * sec)

    s = a * np.sin(2.0 * np.pi * freq * n / fs)

    max_num = 32767.0 / np.max(np.abs(s))
    s = [int(x * max_num) for x in s]

    bin_data = struct.pack('h' * len(s), *s)

    w = wave.Wave_write(filename)
    w.setparams((1, 2, fs, len(bin_data), 'NONE', 'not compressed'))
    w.writeframes(bin_data)
    w.close()

create_wav("sounds/do.wav", TONES["C4"])
create_wav("sounds/re.wav", TONES["D4"])
create_wav("sounds/mi.wav", TONES["E4"])