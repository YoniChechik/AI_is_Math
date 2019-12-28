from build_site import build_site
from file_converter import run_on_all_classes,run_on_class_dir_list

do_py2ipynb = 0
do_ppt=1

# dir_list = [r'C:\Users\chech\Desktop\AI_is_Math\c_10_neural_networks_basics',
# r'C:\Users\chech\Desktop\AI_is_Math\c_09_stereo']
# run_on_class_dir_list(dir_list, do_py2ipynb=do_py2ipynb, do_ppt=do_ppt)
run_on_all_classes(do_py2ipynb=do_py2ipynb, do_ppt=do_ppt)

build_site()
