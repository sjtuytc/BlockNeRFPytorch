_base_ = './tankstemple_base.py'

expname = 'sep14_waymo_five_images'

data = dict(
    datadir='data/sep13_block0/dense',
    factor=2,
    movie_render_kwargs={ # not tuned well
        'scale_r': 1.0,
        'scale_f': 0.8,
        'zrate': 2.0,
        'zdelta': 0.5,
    }
)

fine_train = dict(
    N_iters=30000, # 30k is for quick validation
)