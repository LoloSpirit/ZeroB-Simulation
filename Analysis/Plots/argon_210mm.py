import numpy as np
from TOF_Spectra.tof_spectrum_plotter import plot, PeakSettings, Transformation, ZoomInSettings


files = ['../Output/tof_Ar1-4+_1000eV_210mm.dat']
peak_settings = PeakSettings(match_peaks=True, normalize=True, min_height_percent=.0001, width=1, wlen=50)
plot(files, max_time=4096, interval=[1500, 3800], peak_settings=peak_settings, colors=['black'])
plot(files, max_time=3, interval=[1300, 3100], peak_settings=peak_settings, colors=['black'])

def transform_function(p, a, b):
    p = np.array(p)
    return a * p ** 2 + b
original_points = np.array([1480, 1713, 2080,2919])
target_points = np.array([10, 13, 20, 40])

transformation = Transformation(transform_function, original_points, target_points, 1)

zoom = ZoomInSettings(enabled=True, xlim=(8,22))
plot(files, transformation=transformation, peak_settings=peak_settings, interval=[1300, 3100], zoom_settings=zoom)