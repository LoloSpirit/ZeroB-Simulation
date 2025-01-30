import numpy as np
from TOF_Spectra.tof_spectrum_plotter import plot, PeakSettings, Transformation, ZoomInSettings

files = ['../Output/tof_Ar1-4+_1000eV_410mm.dat']
peak_settings = PeakSettings(match_peaks=True, normalize=True, min_height_percent=.001, width=2, wlen=50)
plot(files, max_time=4, interval=[1500, 3800], peak_settings=peak_settings)

files = ['../Output/tof_Ar1-4+_1000eV_410mm.dat', '../Output/tof_Ar1-4+_1000eV_210mm.dat']
peak_settings = PeakSettings(match_peaks=True, normalize=True, min_height_percent=.001, width=2, wlen=50)
plot(files, max_time=4, interval=[1500, 3800], peak_settings=peak_settings)

def transform_function(p, a, b):
    p = np.array(p)
    return a * p ** 2 + b
original_points = np.array([1828, 2104, 2565, 3600])
target_points = np.array([10, 13, 20, 40])

transformation = Transformation(transform_function, original_points, target_points, 1)

zoom = ZoomInSettings(enabled=True, xlim=(8,22))
plot(files, transformation=transformation, peak_settings=peak_settings, interval=[1500, 3800], zoom_settings=zoom)