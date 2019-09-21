from py2ipynb import py2ipynb
from ppt2pdf import PPTtoPDF
import os


def run_on_all(do_py2ipynb=1, do_py_exec=1, do_ppt=1):
    # get all git cass dirs - starting with "p_"
    cwd = os.getcwd()
    git_main_dirs_cwd = os.path.join(cwd, "..")
    git_class_subdirs = [x for x in os.listdir(
        git_main_dirs_cwd) if x.startswith("p_")]

    for dir_name in git_class_subdirs:
        fp = os.path.join(git_main_dirs_cwd, dir_name)
        run_on_one_dir(fp, do_py2ipynb=do_py2ipynb,
                       do_py_exec=do_py_exec, do_ppt=do_ppt)

        # run on "ex#" dir
        ex_subdirs = [x for x in os.listdir(fp) if x.startswith("ex")]
        for ex_subdir in ex_subdirs:
            fp = os.path.join(fp, ex_subdir)
            # no need to execute the nb
            run_on_one_dir(fp, do_py2ipynb=do_py2ipynb,
                           do_py_exec=0, do_ppt=do_ppt)


def run_on_dir_list(dir_list, do_py2ipynb=1, do_py_exec=1, do_ppt=1):
    for fp in dir_list:
        run_on_one_dir(fp, do_py2ipynb=do_py2ipynb,
                       do_py_exec=do_py_exec, do_ppt=do_ppt)


def run_on_one_dir(fp, do_py2ipynb=1, do_py_exec=1, do_ppt=1):

    print("\n===== IN DIR: " + fp + " =====\n")
    for fn in os.listdir(fp):

        fn_no_ext = fn.split(".")[0]

        # make .pptx -> .pdf
        if fn.endswith(".pptx") and do_ppt:
            print("converting pptx: \n" + fn)
            PPTtoPDF(os.path.join(fp, fn), os.path.join(fp, fn_no_ext+".pdf"))

        # make .py -> .ipynb and compile ipynb
        elif fn.endswith(".py") and do_py2ipynb:
            out_ipynb = os.path.join(fp, fn_no_ext+".ipynb")

            print("converting .py 2 .ipynb: \n" + fn)
            py2ipynb(os.path.join(fp, fn), out_ipynb)

            if do_py_exec:
                print("executing .ipynb: \n" + fn)
                os.system(
                    "jupyter nbconvert --ExecutePreprocessor.timeout=60 --to notebook --execute --inplace \""+out_ipynb+"\"")


if __name__ == "__main__":
    # run_on_dir_list(dir_list, do_py2ipynb=1, do_py_exec=1, do_ppt=1)
    run_on_all(do_py2ipynb=1, do_py_exec=1, do_ppt=0)
