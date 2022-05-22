from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


def waveform_plot(samples):
    plt.plot(np.arange(0, samples.shape[0], 1), samples)


def spectrogram_plot(samples, sample_rate):
    frequencies, times, my_spectrogram = signal.spectrogram(samples, sample_rate, scaling='spectrum', window=('hann', ))
    plt.pcolormesh(times, frequencies, np.log10(my_spectrogram))
    plt.ylabel('Частота [Гц]')
    plt.xlabel('Время [с]')


def denoise(samples, sample_rate, cutoff_freuency, passes=1):
    z = signal.savgol_filter(samples, 101, 2)
    # Get parameters for filter function
    b, a = signal.butter(3, cutoff_freuency / sample_rate)
    # Lowpass filter
    zi = signal.lfilter_zi(b, a)
    for i in range(passes):
        z, _ = signal.lfilter(b, a, z, zi=zi * z[0])
    return z


def to_pcm(y):
    return np.int16(y / np.max(np.abs(y)) * 32767)


if __name__ == '__main__':
    dpi = 400
    cutoff_freuency = 2000

    sample_rate, samples = wavfile.read('src/piano.wav')
    plt.figure(dpi=dpi)
    # waveform_plot(samples)
    spectrogram_plot(samples, sample_rate)
    plt.savefig('out/spectrogram.png', dpi=dpi)
    plt.clf()
    denoised_0 = denoise(samples, sample_rate, cutoff_freuency=2000, passes=0)
    spectrogram_plot(denoised_0, sample_rate)
    plt.savefig('out/denoised_spectrogram_0.png', dpi=dpi)
    plt.clf()
    denoised = denoise(samples, sample_rate, cutoff_freuency=2000)
    spectrogram_plot(denoised, sample_rate)
    plt.savefig('out/denoised_spectrogram_1.png', dpi=dpi)
    plt.clf()
    wavfile.write('out/denoised1.wav', sample_rate, to_pcm(denoised))
    denoised_2 = denoise(samples, sample_rate, cutoff_freuency=2000, passes=2)
    spectrogram_plot(denoised_2, sample_rate)
    plt.savefig('out/denoised_spectrogram_2.png', dpi=dpi)
    plt.clf()
    wavfile.write('out/denoised2.wav', sample_rate, to_pcm(denoised))
