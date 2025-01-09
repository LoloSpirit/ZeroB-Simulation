import re
from matplotlib import pyplot as plt

with open(file='data.txt') as f:
    data = f.read()

pattern = r"TOF\((\d+\.\d+) usec\)"
tof_values = re.findall(pattern, data)
tof = [float(tof) for tof in tof_values]
cutoff = max(tof) / 2 # usec
tof = [tof for tof in tof if tof > cutoff]

res = 1000
plt.hist(tof, bins=res, edgecolor='black', color = 'black')
plt.title('Time of Flight Spectrum')
plt.xlabel('TOF (usec)')
plt.ylabel('Counts')
plt.grid(True)
plt.show()
