from py2ipynb import py2ipynb
from ppt2pdf import PPTtoPDF
import os
import zipfile

def run_on_all_classes(do_py2ipynb=1, do_py_exec=1, do_ppt=1):
    # ==== get all git cass dirs - starting with "c_"
    cwd = os.getcwd()
    git_main_dirs_cwd = os.path.abspath(os.path.join(cwd, ".."))
    git_class_subdirs = [x for x in os.listdir(
        git_main_dirs_cwd) if x.startswith("c_")]

    for dir_name in git_class_subdirs:
        fp = os.path.join(git_main_dirs_cwd, dir_name)
        run_on_one_class_dir(fp, do_py2ipynb=do_py2ipynb,
                       do_py_exec=do_py_exec, do_ppt=do_ppt)


def run_on_class_dir_list(dir_list, do_py2ipynb=1, do_py_exec=1, do_ppt=1):
    for fp in dir_list:
        run_on_one_class_dir(fp, do_py2ipynb=do_py2ipynb,
                       do_py_exec=do_py_exec, do_ppt=do_ppt)
        


def run_on_one_class_dir(fp, do_py2ipynb=1, do_py_exec=1, do_ppt=1):

    print("\n===== IN DIR: " + fp + " =====\n")

    # === run on class dir data
    run_on_one_dir(fp, do_py2ipynb=do_py2ipynb, do_py_exec=do_py_exec, do_ppt=do_ppt)

    # ==== run on "ex#" dir
    if do_py2ipynb:
        ex_subdirs = [x for x in os.listdir(fp) if (x.startswith("ex") and os.path.isdir(os.path.join(fp,x)))]
        for ex_subdir in ex_subdirs:

            fp_ex = os.path.join(fp, ex_subdir)

            # ==== only convert py2ipynb, no need to execute the nb
            run_on_one_dir(fp_ex, do_py2ipynb=1, do_py_exec=0, do_ppt=0)

            # ==== zip ex files
            print("- zipping ex \n")
            with zipfile.ZipFile(os.path.join(fp_ex,ex_subdir + '.zip'), 'w') as myzip:
                for f in os.listdir(fp_ex):
                    if not f.endswith(".zip") and f!="." and f!="..":   
                        myzip.write(os.path.join(fp_ex,f),f)


def run_on_one_dir(fp, do_py2ipynb=1, do_py_exec=1, do_ppt=1):

    # ==== run on all files
    for fn in os.listdir(fp):

        fn_no_ext = fn.split(".")[0]

        # ==== make .pptx -> .pdf
        if fn.endswith(".pptx") and do_ppt:
            print("- converting pptx: \n" + fn)
            docs_fp = fp.replace("AI_is_Math",os.path.join("AI_is_Math","docs","pages"))

            if not os.path.exists(docs_fp):
                os.mkdir(docs_fp)
                
            PPTtoPDF(os.path.join(fp, fn), os.path.join(docs_fp, fn_no_ext+".pdf"))

        # ==== make .py -> .ipynb and compile ipynb
        elif fn.endswith(".py") and do_py2ipynb:
            out_ipynb = os.path.join(fp, fn_no_ext+".ipynb")

            print("- converting .py 2 .ipynb:  " + fn+"\n")
            py2ipynb(os.path.join(fp, fn), out_ipynb)

            if do_py_exec:
                print("- executing .ipynb: " + fn+"\n")
                os.system(
                    "jupyter nbconvert --ExecutePreprocessor.timeout=120 --to notebook --execute --inplace \""+out_ipynb+"\"")
    
if __name__ == "__main__":
    dir_list = [r'C:\Users\chech\Desktop\AI_is_Math\c_03_edge_detection']
    run_on_class_dir_list(dir_list, do_py2ipynb=0, do_ppt=1)
    # run_on_all_classes(do_py2ipynb=1, do_ppt=1)
