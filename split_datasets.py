import splitfolders

input_path_colors_2 = 'datasets/data/raw/colors_2/color'
input_path_vehicle_type = 'datasets/data/raw/vehicle_type'

output_path_colors_2 = 'datasets/data/split/colors_2'
output_path_vehicle_type = 'datasets/data/split/vehicle_type'

splitfolders.ratio(input_path_colors_2, output=output_path_colors_2,
                   seed=1337, ratio=(0.7, 0.15, 0.15),
                   group_prefix=None)

splitfolders.ratio(input_path_vehicle_type, output=output_path_vehicle_type,
                   seed=1337, ratio=(0.7, 0.15, 0.15),
                   group_prefix=None)
