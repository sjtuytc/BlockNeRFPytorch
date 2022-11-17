_base_ = '../default.py'
seq_name = 'ape'
seq_id = 1
expname = f'{seq_name}_nov11_'
pose_expname = 'bayes_nerf_v1_12'
basedir = 'logs/linemod'

data = dict(
    datadir='./data/linemod',
    dataset_type='linemod',
    white_bkgd=True,
    seq_name=seq_name,
    seq_id=1,
    width_max=90,
    height_max=90,
    load2gpu_on_the_fly=True,
)

# coarse_train = dict(
#     N_iters=0, # use this in global rendering only, remove this in canonical rendering
# )

fine_train = dict(
    # ray_sampler='flatten', # use this in global rendering only, remove this in canonical rendering
    N_iters=50*(10**4),
)

# voxel_num=32**3
# coarse_model_and_render = dict(
#     num_voxels_rgb=voxel_num,
#     num_voxels_base_rgb=voxel_num,
#     num_voxels_density=voxel_num,
#     num_voxels_base_density=voxel_num,
# )
# fine_model_and_render = dict(
#     num_voxels_rgb=voxel_num,
#     num_voxels_base_rgb=voxel_num,
#     num_voxels_density=voxel_num,
#     num_voxels_base_density=voxel_num,
#     # rgbnet_dim=0,
# )