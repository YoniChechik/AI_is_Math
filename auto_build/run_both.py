from build_site import build_site
from file_converter import run_on_all_classes,run_on_class_dir_list

do_py2ipynb = 1
do_ppt=0

dir_list = [r'C:\Users\chech\Desktop\AI_is_Math\c_11_neural_networks_2']
run_on_class_dir_list(dir_list, do_py2ipynb=do_py2ipynb, do_ppt=do_ppt)
# run_on_all_classes(do_py2ipynb=do_py2ipynb, do_ppt=do_ppt)

build_site()
