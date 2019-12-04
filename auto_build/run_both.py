from build_site import build_site
from file_converter import run_on_all_classes,run_on_class_dir_list

dir_list = [r'C:\Users\chech\Desktop\AI_is_Math\c_05_image_formation']
run_on_class_dir_list(dir_list, do_py2ipynb=0, do_ppt=1)
# run_on_all_classes(do_py2ipynb=0, do_ppt=1)

build_site()
