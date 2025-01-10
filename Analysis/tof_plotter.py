from matplotlib import pyplot as plt

tof = []
with open(file='Output/tof.txt') as f:
    for line in f:
        try:
            tof.append(float(line.strip()))
        except ValueError:
            pass

# cutoff = max(tof) / 2 # usec
#tof = [tof for tof in tof if tof > cutoff]

res = 1000
plt.hist(tof, bins=res, edgecolor='black', color = 'black')
plt.title('Simulated Time of Flight Spectrum')
plt.xlabel('TOF (usec)')
plt.ylabel('Counts')
plt.grid(True)
plt.show()
