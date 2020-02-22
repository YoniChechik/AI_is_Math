# %%
import matplotlib.pyplot as plt
import numpy as np
import warnings

def fftPlot(sig, dt=None, block=False, plot=True):
    # here it's assumes analytic signal (real signal...)- so only half of the axis is required

    if dt is None:
        dt = 1
        t = np.arange(0, sig.shape[-1])
        xLabel = 'samples'
    else:
        t = np.arange(0, sig.shape[-1]) * dt
        xLabel = 'freq [Hz]'

    if sig.shape[0] % 2 != 0:
        warnings.warn("signal prefered to be even in size, autoFixing it...")
        t = t[0:-1]
        sig = sig[0:-1]

    sigFFT = np.fft.fft(sig) / t.shape[0]  # divided by size t for coherent magnitude

    freq = np.fft.fftfreq(t.shape[0], d=dt)

    # plot analytic signal - right half of freq axis needed only...
    firstNegInd = np.argmax(freq < 0)
    freqAxisPos = freq[0:firstNegInd]
    sigFFTPos = 2 * sigFFT[0:firstNegInd]  # *2 because of magnitude of analytic signal

    if plot:
        plt.figure()
        plt.plot(freqAxisPos, np.abs(sigFFTPos))
        plt.xlabel(xLabel)
        plt.ylabel('mag')
        plt.title('Analytic FFT plot')
        plt.show(block=block)

    return sigFFTPos, freqAxisPos


#%%
dt = 1 / 1000
f0 = 10 # 1 / dt / 4

t = np.arange(0, 1 + dt, dt)
sig = np.sin(2 * np.pi * f0 * t+100) + 10 * np.sin(2 * np.pi * f0 / 2 * t)
sig = np.sin(2 * np.pi * f0 * t) #+ 10 * np.sin(2 * np.pi * f0 / 2 * t)

plt.figure()
plt.plot(t,sig)
#%%
fftPlot(sig, dt=dt, block=True)


# %%
