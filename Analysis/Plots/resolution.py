import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

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
plot(files, transformation=transformation, peak_settings=peak_settings, interval=[350, 3200], product_labels=ions)


# Fit peaks and determine resolution
resolution = []

def gauss(x, a, b, x0):
    return a * np.exp(-1 * b * (x - x0) ** 2)

# load
x, y = np.loadtxt('../Output/test_masses_1-30u.dat', unpack=True)
x = x[350:3200]
y = y[350:3200]

# transform into mass spectrum
params, _ = curve_fit(transformation.function, transformation.original_points, transformation.target_points)
x = transformation.function(x, *params)

# smooth data
y = gaussian_filter1d(y, 2)
peaks, _ = find_peaks(y, height=10)
plt.plot(x, y, color='blue')

# fit each peak individually
for i, peak in enumerate(peaks):
    window_size = .5
    mask = (x > x[peak] - window_size) & (x < x[peak] + window_size)

    x_peak = x[mask]
    y_peak = y[mask]

    # initial guess
    p0 = [max(y_peak), 3, x[peak]]

    try:
        popt, _ = curve_fit(gauss, x_peak, y_peak, p0=p0)
        fit_a, fit_b, fit_x_0 = popt
        # find intersections with half maximum
        fwhm = 2 * np.sqrt(np.log(2) / fit_b)
        plt.axvspan(x[peak] - fwhm/2, x[peak] + fwhm/2, alpha=0.5, color='red')

        mass = x[peak]
        res = mass / fwhm
        print(fwhm, res)
        resolution.append(res)

        plt.plot(x_peak, gauss(x_peak, *popt), color='black', label=f"{i}")
    except RuntimeError:
        print(f"Could not fit peak at x={x[peak]:.1f}")

plt.xlabel(r"m/q")
plt.ylabel("Counts")
plt.show()

def fit(x, a, b):
    return a * 1 / x + b

x = x[peaks]
x_fine = np.linspace(min(x), max(x), 100)

files = ['../Output/test_masses_1-60u_fine_210.dat', '../Output/test_masses_1-60u_210.dat']
peak_settings = PeakSettings(min_height_percent=.001, width=2, wlen=50)
plot(files, max_time=4096, interval=[350, 4096], peak_settings=peak_settings)
# fit resolutions
params, _ = curve_fit(fit, x, resolution, p0=[1, 0])
a_fit, b_fit = params
plt.figure(figsize=(8, 5))
plt.plot(x_fine, fit(x_fine, *params), color='gray', label=fr"Fit: $R(m) = \frac{{{a_fit:.2f}}}{{m}} + {b_fit:.2f}$")
plt.xlabel(r"m/q [$u$/$e$]")
plt.ylabel("R")
plt.scatter(x, resolution, marker='x', linewidth=1, color='black', label="Simulierte Daten")
plt.legend()
plt.show()

def transform_function(p, a, b):
    p = np.array(p)
    return a * p ** 2 + b
original_points = np.array([451, 851, 1428, 3133])
target_points = np.array([.5, 2, 6, 30])

# load experimental data for comparison
x, y = np.loadtxt('../../../DataAnalysis/TOF_Spectra/MCA_Data/restgas.dat', unpack=True)
x = x[:2800]
original_points = np.array([126, 175, 396, 406])
target_points = np.array([1, 2, 17, 18])
transformation = Transformation(transform_function, original_points, target_points)

transformation = Transformation(transform_function, original_points, target_points, 1)
params, _ = curve_fit(transformation.function, transformation.original_points, transformation.target_points)
x = transformation.function(x, *params)

# smooth data
y = gaussian_filter1d(y, 1)
peaks, _ = find_peaks(y, height=200, width=1, wlen=100)
plt.plot(x, y, color='blue')

zoom = ZoomInSettings(enabled=True, xlim=(8,22))
plot(files, transformation=transformation, peak_settings=peak_settings, interval=[350, 4096], product_labels=ions)
# Fit peaks and determine resolution
resolution = []

# fit each peak individually
for i, peak in enumerate(peaks):
    window_size = .5
    mask = (x > x[peak] - window_size) & (x < x[peak] + window_size)

    x_peak = x[mask]
    y_peak = y[mask]

    # initial guess
    p0 = [max(y_peak), 3, x[peak]]

    try:
        popt, _ = curve_fit(gauss, x_peak, y_peak, p0=p0)
        fit_a, fit_b, fit_x_0 = popt
        # find intersections with half maximum
        fwhm = 2 * np.sqrt(np.log(2) / fit_b)
        plt.axvspan(x[peak] - fwhm/2, x[peak] + fwhm/2, alpha=0.5, color='red')

        mass = x[peak]
        res = mass / fwhm
        print(f'{mass}: width({fwhm}), res({res})')
        resolution.append(res)

        plt.plot(x_peak, gauss(x_peak, *popt), color='black', label=f"{i}")
    except RuntimeError:
        print(f"Could not fit peak at x={x[peak]:.1f}")

plt.xlabel(r"t in $\mu$s")
plt.ylabel("Counts")
plt.show()

x = x[peaks]
plt.scatter(x, resolution, marker='x', linewidth=1, color='black', label="Simulierte Daten")
plt.legend()
plt.show()