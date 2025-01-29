import numpy as np
from matplotlib import pyplot as plt

files = ['Output/background_ions_410mm.txt']
colors = ['black', 'red', 'blue', 'green', 'orange', 'purple']
res = 4096
plt.figure(figsize=(10.5, 5))

for file in files:
    tof = []
    extraction_delay = 0
    with open(file=file) as f:
        for line in f:
            if 'Extraction delay' in line:
                extraction_delay = float(line.split(':')[-1].strip())
            try:
                values = line.split(',')
                if len(values) > 1:
                    # exclude splats not on the detector
                    if float(values[1].strip()) < 190:
                        continue
                tof.append(float(values[0].strip()))
            except ValueError:
                pass

    # compensate for extraction delay
    tof = [t - extraction_delay for t in tof]

    # Create binned data (same logic as in the histogram, but for line plot)
    bin_counts, bin_edges = np.histogram(tof, bins=res, range=(min(tof), max(tof)))

    # Get the bin centers for the line plot
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

    # Plot the binned data as a line plot
    color = colors.pop(0)
    plt.plot(bin_centers, bin_counts, color=color, alpha=1, label=file.split('/')[-1].split('.')[0])

plt.grid(False)
plt.xlabel(r't in $\mu$s')
legend = plt.legend()
for line in legend.get_lines():
    line.set_linewidth(4)
plt.ylabel('Counts')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
