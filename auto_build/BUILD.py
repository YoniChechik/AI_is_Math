import os

from auto_build import file_converter
from auto_build.build_site import build_site

do_ppt = 0  # DON'T CHANGE if we don't have office
run_ipynb = 0
is_convert_ipynb_to_html = 1

main_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
dir_list = [
    "c_01_intro_to_CV_and_Python",
    "c_02a_basic_image_processing",
    # "c_02b_filtering_and_resampling",
    # "c_03_edge_detection",
    # "c_04a_curve_fitting",
    # "c_04b_hough_transform",
    # "c_05_image_formation",
    # "c_06_geometric_transformation",
    # "c_07_camera_calibration",
    # "c_08_features",
    # "c_09_stereo",
    # "c_10_neural_networks_basics",
    # "c_11_neural_networks_2",
]


dir_list = [os.path.join(main_path, dir_i) for dir_i in dir_list]

file_converter.run_on_class_dir_list(dir_list, do_ppt, run_ipynb)

build_site(dir_list, is_convert_ipynb_to_html)
