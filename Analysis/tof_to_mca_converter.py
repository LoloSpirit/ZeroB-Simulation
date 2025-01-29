import numpy as np


def convert_to_mca(input_file, output_file, channel_count, max_time):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    tof = []
    extraction_delay = 0
    with open(file=input_file) as f:
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

    # account for delay
    adjusted_times = [time - extraction_delay for time in tof]

    channel_ranges = np.linspace(0, max_time, channel_count)

    # create a list to store counts for each channel
    channel_counts = [0] * channel_count

    # count how many times fall into each channel
    for time in adjusted_times:
        if time < max_time:  # ensure times are within the max range
            channel_index = np.searchsorted(channel_ranges, time, side='right') - 1
            channel_counts[channel_index] += 1

    # write the result to the output file
    with open(output_file, 'w') as f:
        for i, count in enumerate(channel_counts):
            f.write(f"{i} {count}\n")


input_file = 'Output/tof_Ar1-4+_1000eV_210mm.txt'
output_file = 'Output/tof_Ar1-4+_1000eV_210mm.dat'
convert_to_mca(input_file, output_file, 4096, 2.5)# in usec

input_file = 'Output/tof_Ar1-4+_1000eV_410mm.txt'
output_file = 'Output/tof_Ar1-4+_1000eV_410mm.dat'
convert_to_mca(input_file, output_file, 4096, 4)# in usec
