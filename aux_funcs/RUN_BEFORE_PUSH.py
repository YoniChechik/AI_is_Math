from py2ipynb import py2ipynb
from ppt2pdf import PPTtoPDF
import os

DO_PPT = 1
DO_PY = 0


cwd = os.getcwd()
git_dirs = os.path.join(cwd,"..")

git_class_subdirs = [x for x in os.listdir(git_dirs) if ( os.path.isdir(os.path.join(git_dirs,x)) and x.startswith("p_") ) ]
for dir_name in git_class_subdirs:
    fp = os.path.join(git_dirs,dir_name)

    # if os.path.isdir(fp): #if dir 'raw' exists
    print("===== IN DIR: " + fp + " =====")
    for fn in os.listdir(fp):

        fn_no_ext = fn.split(".")[0]
        if fn.endswith(".pptx") and DO_PPT:
            print("converting pptx: "+ fn)
            PPTtoPDF(os.path.join(fp,fn),os.path.join(fp,fn_no_ext+".pdf"))
        elif fn.endswith(".py") and DO_PY:
            out_ipynb = os.path.join(fp,fn_no_ext+".ipynb")

            print("converting .py 2 .ipynb: "+ fn)
            py2ipynb(os.path.join(fp,fn), out_ipynb)
            
            print("executing .ipynb : "+ fn)
            os.system("jupyter nbconvert --ExecutePreprocessor.timeout=60 --to notebook --execute --inplace \""+out_ipynb+"\"")