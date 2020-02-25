from build_site import build_site
from file_converter import run_on_all_classes,run_on_class_dir_list
import os


do_py2ipynb = 1
do_ppt=0

main_path = r"C:\Users\chech\Desktop\AI_is_Math"
dir_list = [
    # 'c_01_intro_to_CV_and_Python',
    # 'c_02a_basic_image_processing',
    # 'c_02b_filtering_and_resampling',
    'c_03_edge_detection',
    # 'c_04_curve_fitting',
    # 'c_05_image_formation',
    # 'c_06_geometric_transformation',
    # 'c_07_camera_calibration',
    # 'c_08_features',
    # 'c_09_stereo',
    # 'c_10_neural_networks_basics',
    # 'c_11_neural_networks_2'
    ]


dir_list = [os.path.join(main_path,dir_i) for dir_i in dir_list]

run_on_class_dir_list(dir_list, do_py2ipynb=do_py2ipynb, do_ppt=do_ppt)
# run_on_all_classes(do_py2ipynb=do_py2ipynb, do_ppt=do_ppt)

build_site(dir_list)
