import numpy as np

def convert_to_grid(input_file, output_file, step=0.020094):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    ys = []
    zs = []

    # Process input data
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 3:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())

            if x < 190:
                continue
            ys.append(y)
            zs.append(z)

    resolution = 280

    # create a grid
    z_min, z_max = -40, 40
    y_min, y_max = -40, 40

    # Create a meshgrid
    y_grid = np.linspace(y_min, y_max, resolution)
    z_grid = np.linspace(z_min, z_max, resolution)
    Y, Z = np.meshgrid(y_grid, z_grid)

    counts = np.zeros_like(Y)

    for i in range(len(zs)):

        iy = np.abs(y_grid - ys[i]).argmin()
        iz = np.abs(z_grid - zs[i]).argmin()

        counts[iy, iz] += 1

    with open(output_file, 'w') as f:
        # meshgrid to file
        for i,y in enumerate(y_grid):
            for j,z in enumerate(z_grid):
                if counts[i,j] > 0:
                    f.write(f"{y},{z},{counts[i,j]}\n")


input_file = 'Output/posdata_0,2eV.txt'
output_file = 'Output/posdata_0,2eV.cod'
convert_to_grid(input_file, output_file)

input_file = 'Output/pos_data_410.txt'
output_file = 'Output/pos_data_410.cod'
convert_to_grid(input_file, output_file)

input_file = 'Output/positions.txt'
output_file = 'Output/positions.cod'
convert_to_grid(input_file, output_file)

input_file = 'Output/pos_data_fine.txt'
output_file = 'Output/pos_data_fine.cod'
convert_to_grid(input_file, output_file)