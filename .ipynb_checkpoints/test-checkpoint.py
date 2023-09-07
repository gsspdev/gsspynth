import numpy as np
import matplotlib.pylab as plt

# np.sin().freq()

x = np.linspace(-np.pi, np.pi, 201)

# Parameters for the sine wave
amp = 1.0  # amp of the sine wave
freq = 440  # freq in Hz
dur = 5.0   # dur of the sine wave in seconds
smp= 44100  # Number of samples per second (sampling rate)

# Generate time values from 0 to dur at the specified sample rate
t = np.linspace(0, dur, int(smp * dur), endpoint=False)

# Generate the sine wave
sine_wave = amp * np.sin(2 * np.pi * freq * t)

plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()


# plt.plot(t, sine_wave)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('Sine Wave')
# plt.grid(True)
# plt.show()
