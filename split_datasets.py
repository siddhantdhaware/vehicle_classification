import splitfolders

input_path_colors_2 = 'datasets/data/raw/colors_2/color'
input_path_vehicle_type = 'datasets/data/raw/vehicle_type'

output_path_colors_2 = 'datasets/data/split/colors_2'
output_path_vehicle_type = 'datasets/data/split/vehicle_type'

input_path_zenodo = 'datasets/data/raw/vehicles_zenodo'
output_path_zenodo = 'datasets/data/split/vehicles_zenodo'

input_path_vtid = 'datasets/data/raw/VTID2'
output_path_vtid = 'datasets/data/split/VTID2'

# splitfolders.ratio(input_path_colors_2, output=output_path_colors_2,
#                    seed=1337, ratio=(0.7, 0.15, 0.15),
#                    group_prefix=None)

# splitfolders.ratio(input_path_vehicle_type, output=output_path_vehicle_type,
#                    seed=1337, ratio=(0.7, 0.15, 0.15),
#                    group_prefix=None)

# splitfolders.ratio(input_path_zenodo, output=output_path_zenodo,
#                    seed=1337, ratio=(0.7, 0.15, 0.15),
#                    group_prefix=None)

splitfolders.ratio(input_path_vtid, output=output_path_vtid,
                   seed=1337, ratio=(0.7, 0.15, 0.15),
                   group_prefix=None)
