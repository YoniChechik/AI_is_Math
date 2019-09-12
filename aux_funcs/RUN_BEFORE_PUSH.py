from py2ipynb import py2ipynb
from ppt2pdf import PPTtoPDF
import os

DO_PPT = 1
DO_PY = 0

#get all git cass dirs - starting with "p_"
cwd = os.getcwd()
git_main_dirs_cwd = os.path.join(cwd,"..")
git_class_subdirs = [x for x in os.listdir(git_main_dirs_cwd) if ( os.path.isdir(os.path.join(git_main_dirs_cwd,x)) and x.startswith("p_") ) ]

for dir_name in git_class_subdirs:
    fp = os.path.join(git_main_dirs_cwd,dir_name)

    print("===== IN DIR: " + fp + " =====")
    for fn in os.listdir(fp):

        fn_no_ext = fn.split(".")[0]

        # make .pptx -> .pdf
        if fn.endswith(".pptx") and DO_PPT:
            print("converting pptx: "+ fn)
            PPTtoPDF(os.path.join(fp,fn),os.path.join(fp,fn_no_ext+".pdf"))

        # make .py -> .ipynb and compile ipynb
        elif fn.endswith(".py") and DO_PY:
            out_ipynb = os.path.join(fp,fn_no_ext+".ipynb")

            print("converting .py 2 .ipynb: "+ fn)
            py2ipynb(os.path.join(fp,fn), out_ipynb)
            
            print("executing .ipynb : "+ fn)
            os.system("jupyter nbconvert --ExecutePreprocessor.timeout=60 --to notebook --execute --inplace \""+out_ipynb+"\"")