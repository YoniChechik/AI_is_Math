import os
import zipfile

from ppt2pdf import PPTtoPDF


def run_on_all_classes(do_ppt=1):
    # ==== get all git class dirs - starting with "c_"
    cwd = os.getcwd()
    git_main_dirs_cwd = os.path.abspath(os.path.join(cwd, ".."))
    git_class_subdirs = [x for x in os.listdir(git_main_dirs_cwd) if x.startswith("c_")]

    for dir_name in git_class_subdirs:
        fp = os.path.join(git_main_dirs_cwd, dir_name)
        run_on_one_class_dir(fp, do_ppt=do_ppt)


def run_on_class_dir_list(dir_list, do_ppt=1):
    for fp in dir_list:
        run_on_one_class_dir(fp, do_ppt=do_ppt)


def run_on_one_class_dir(fp, do_ppt=1):
    print("\n===== IN DIR: " + fp + " =====\n")

    run_on_one_dir(fp, do_ppt=do_ppt)

    build_ex_dir(fp)


def build_ex_dir(fp):
    ex_subdirs = [
        x
        for x in os.listdir(fp)
        if (x.startswith("ex") and os.path.isdir(os.path.join(fp, x)))
    ]
    for ex_subdir in ex_subdirs:
        fp_ex = os.path.join(fp, ex_subdir)

        # ==== zip ex files
        print("- zipping ex \n")
        with zipfile.ZipFile(os.path.join(fp_ex, ex_subdir + ".zip"), "w") as myzip:
            for f in os.listdir(fp_ex):
                if not f.endswith(".zip") and f != "." and f != "..":
                    myzip.write(os.path.join(fp_ex, f), f)


def run_on_one_dir(fp: str, do_ppt=1):
    # ==== run on all files
    for fn in os.listdir(fp):
        fn_no_ext = fn.split(".")[0]

        # ==== make .pptx -> .pdf
        if fn.endswith(".pptx") and do_ppt:
            print("- converting pptx: \n" + fn)
            docs_fp = fp.replace(
                "AI_is_Math", os.path.join("AI_is_Math", "docs", "pages")
            )

            if not os.path.exists(docs_fp):
                os.mkdir(docs_fp)

            PPTtoPDF(os.path.join(fp, fn), os.path.join(docs_fp, fn_no_ext + ".pdf"))

        # === ipynb
        elif fn.endswith(".ipynb"):
            fp_ipynb = os.path.join(fp, fn)
            print("- executing .ipynb: " + fn + "\n")
            os.system(
                f'jupyter nbconvert --ExecutePreprocessor.timeout=120 --to notebook --execute --inplace "{fp_ipynb}"'
            )
