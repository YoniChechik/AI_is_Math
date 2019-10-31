from py2ipynb import py2ipynb
from ppt2pdf import PPTtoPDF
import os
import zipfile
import shutil

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

    # ==== mkdir site_docs
    site_docs_dir = os.path.join(fp, "site_docs")
    if not os.path.exists(site_docs_dir):
        os.mkdir(site_docs_dir)

    # === run on class dir data
    run_on_one_dir(fp, site_docs_dir, do_py2ipynb=do_py2ipynb, do_py_exec=do_py_exec, do_ppt=do_ppt)

    # ==== run on "ex#" dir
    if do_py2ipynb:
        ex_subdirs = [x for x in os.listdir(fp) if (x.startswith("ex") and os.path.isdir(os.path.join(fp,x)))]
        for ex_subdir in ex_subdirs:
            
            # ==== mkdir site_docs/ex
            site_docs_ex_dir_path = os.path.join(fp, "site_docs",ex_subdir)
            if not os.path.exists(site_docs_ex_dir_path):
                os.mkdir(site_docs_ex_dir_path)

            fp_ex = os.path.join(fp, ex_subdir)

            # ==== only convert py2ipynb, no need to execute the nb
            run_on_one_dir(fp_ex, site_docs_ex_dir_path, do_py2ipynb=1, do_py_exec=0, do_ppt=0)

            # ==== zip ex files
            print("\n===== zipping ex =====\n")
            with zipfile.ZipFile(os.path.join(site_docs_ex_dir_path,ex_subdir + '.zip'), 'w') as myzip:
                for f in os.listdir(fp_ex):
                    if not f.endswith(".zip") and not os.path.isdir(os.path.join(fp_ex,f)):   
                        myzip.write(os.path.join(fp_ex,f),f)


def run_on_one_dir(fp, site_docs_dir, do_py2ipynb=1, do_py_exec=1, do_ppt=1):
    
    # ==== tmp copy all relevant data to site_docs_dir for executing
    if do_py_exec:
        copied_fp_list = []
        for fn in os.listdir(fp):
            file_fp = os.path.join(fp, fn)
            if not (file_fp.endswith(".py") or
                    file_fp.endswith(".ipynb") or
                    file_fp.endswith(".pdf") or
                    file_fp.endswith(".pptx") or
                    os.path.isdir(file_fp)):
                copied_fp = os.path.join(site_docs_dir, fn)
                shutil.copyfile(file_fp,copied_fp)
                copied_fp_list.append(copied_fp)

    # ==== run on all files
    for fn in os.listdir(fp):

        fn_no_ext = fn.split(".")[0]

        # ==== make .pptx -> .pdf
        if fn.endswith(".pptx") and do_ppt:
            print("converting pptx: \n" + fn)
            PPTtoPDF(os.path.join(fp, fn), os.path.join(site_docs_dir, fn_no_ext+".pdf"))

        # ==== make .py -> .ipynb and compile ipynb
        elif fn.endswith(".py") and do_py2ipynb:
            out_ipynb = os.path.join(site_docs_dir, fn_no_ext+".ipynb")

            print("converting .py 2 .ipynb: \n" + fn)
            py2ipynb(os.path.join(fp, fn), out_ipynb)

            if do_py_exec:
                print("executing .ipynb: \n" + fn)
                os.system(
                    "jupyter nbconvert --ExecutePreprocessor.timeout=60 --to notebook --execute --inplace \""+out_ipynb+"\"")
    
    # ==== remove all tmp copied files
    if do_py_exec:
        for copied_fp in copied_fp_list:
            os.remove(copied_fp)

if __name__ == "__main__":
    # dir_list = [r'C:\Users\chech\Desktop\AI_is_Math\c_01_basic_CV_and_python']
    # run_on_class_dir_list(dir_list, do_py2ipynb=1, do_ppt=1)
    run_on_all_classes(do_py2ipynb=1, do_ppt=1)
