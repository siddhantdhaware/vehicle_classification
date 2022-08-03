import splitfolders

input_path_zenodo = 'datasets/data/raw/Zenodo'
output_path_zenodo = 'datasets/data/split/Zenodo'

input_path_vtid = 'datasets/data/raw/VTID2'
output_path_vtid = 'datasets/data/split/VTID2'

splitfolders.ratio(input_path_zenodo, output=output_path_zenodo,
                   seed=1337, ratio=(0.7, 0.15, 0.15),
                   group_prefix=None)

splitfolders.ratio(input_path_vtid, output=output_path_vtid,
                   seed=1337, ratio=(0.7, 0.15, 0.15),
                   group_prefix=None)
