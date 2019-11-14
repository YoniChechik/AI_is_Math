from build_site import build_site
from file_converter import run_on_all_classes,run_on_class_dir_list

dir_list = [r'C:\Users\jonathanch\Desktop\AI_is_Math\c_02_image_processing']
run_on_class_dir_list(dir_list, do_py2ipynb=1, do_ppt=1)
# run_on_all_classes(do_py2ipynb=1, do_ppt=1)

build_site()
