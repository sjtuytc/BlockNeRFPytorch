_base_ = '../default.py'
basedir = './logs/waymo'
visualize_poses = True
alpha_init = 1e-4
stepsize = 0.5
_mpi_depth = 256
maskout_near_cam_vox = False
pervoxel_lr = False
unbounded_inward = True
if visualize_poses:  # for debugging
    coarse_iter = 600
    fast_color_thres=stepsize/_mpi_depth/5
    weight_distortion = 0.0
else:
    coarse_iter = 0
    fast_color_thres={
            '_delete_': True,
            0   : alpha_init*stepsize/10,
            1500: min(alpha_init, 1e-4)*stepsize/5,
            2500: min(alpha_init, 1e-4)*stepsize/2,
            3500: min(alpha_init, 1e-4)*stepsize/1.5,
            4500: min(alpha_init, 1e-4)*stepsize,
            5500: min(alpha_init, 1e-4),
            6500: 1e-4,
        }

    weight_distortion = 0.01

data = dict(
    dataset_type='waymo',
    inverse_y=True,
    white_bkgd=True,
    rand_bkgd=True,
    unbounded_inward=unbounded_inward,
    load2gpu_on_the_fly=True,
    # bd_factor=None,
)

coarse_train = dict(
    N_iters=coarse_iter,
    pervoxel_lr = pervoxel_lr,
#     ray_sampler='flatten',
)

fine_train = dict(
    N_iters=30000,
    N_rand=4096,
    ray_sampler='flatten',
    weight_distortion=weight_distortion,
    pg_scale=[1000,2000,3000,4000,5000,6000,7000],
    tv_before=1e9,
    tv_dense_before=10000,
    weight_tv_density=1e-6,
    weight_tv_k0=1e-7,
)

coarse_model_and_render = dict(
    maskout_near_cam_vox = maskout_near_cam_vox,
)

fine_model_and_render = dict(
    num_voxels=320**3,
    num_voxels_base=320**3,
    alpha_init=alpha_init,
    stepsize=stepsize,
    fast_color_thres=fast_color_thres,
    world_bound_scale=1,
    contracted_norm='l2',
)