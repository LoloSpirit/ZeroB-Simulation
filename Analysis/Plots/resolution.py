import numpy as np
from TOF_Spectra.tof_spectrum_plotter import plot, PeakSettings, Transformation, ZoomInSettings

ions = []
files = ['../Output/test_masses_1-60u.dat', '../Output/test_masses_1-60u_fine.dat']
peak_settings = PeakSettings(min_height_percent=.001, width=2, wlen=50)
plot(files, max_time=4096, interval=[350, 4096], peak_settings=peak_settings)

def transform_function(p, a, b):
    p = np.array(p)
    return a * p ** 2 + b
original_points = np.array([451, 851, 1428, 3133])
target_points = np.array([.5, 2, 6, 30])

transformation = Transformation(transform_function, original_points, target_points, 1)

zoom = ZoomInSettings(enabled=True, xlim=(8,22))
plot(files, transformation=transformation, peak_settings=peak_settings, interval=[350, 4096], product_labels=ions)

files = ['../Output/test_masses_1-60u_fine_210.dat', '../Output/test_masses_1-60u_210.dat']
peak_settings = PeakSettings(min_height_percent=.001, width=2, wlen=50)
plot(files, max_time=4096, interval=[350, 4096], peak_settings=peak_settings)

def transform_function(p, a, b):
    p = np.array(p)
    return a * p ** 2 + b
original_points = np.array([451, 851, 1428, 3133])
target_points = np.array([.5, 2, 6, 30])

transformation = Transformation(transform_function, original_points, target_points, 1)

zoom = ZoomInSettings(enabled=True, xlim=(8,22))
plot(files, transformation=transformation, peak_settings=peak_settings, interval=[350, 4096], product_labels=ions)