from py2ipynb import py2ipynb
from ppt2pdf import PPTtoPDF
import os

cwd = os.getcwd()
raw_git_dir = os.path.join(cwd,"..","cv_course_raw_git")

# run on all "raw" subdirs in git dir
git_raw_subdirs = [x for x in os.listdir(raw_git_dir) if os.path.isdir(os.path.join(raw_git_dir,x))]
for dir_name in git_raw_subdirs:
    fp = os.path.join(raw_git_dir,dir_name)

    # if os.path.isdir(fp): #if dir 'raw' exists
    print("===== IN DIR: " + fp + " =====")
    for fn in os.listdir(fp):
        # ffp = os.path.join(fp,fn)

        # if fn != "edge_detection.py":
        #     continue

        fn_no_ext = fn.split(".")[0]
        if fn.endswith(".pptx"):
            print("converting pptx: "+ fn)
            # PPTtoPDF(os.path.join(fp,fn),os.path.join(fp,"..",fn_no_ext+".pdf"))
        elif fn.endswith(".py"):
            out_ipynb = os.path.join(fp,fn_no_ext+".ipynb")

            print("converting .py 2 .ipynb: "+ fn)
            py2ipynb(os.path.join(fp,fn), out_ipynb)
            
            print("executing .ipynb : "+ fn)
            # print("jupyter nbconvert --to notebook --execute \""+out_file+"\"")
            # os.system("jupyter nbconvert --ExecutePreprocessor.timeout=60 --to notebook --execute --inplace \""+out_file+"\"")
            os.system("jupyter nbconvert --ExecutePreprocessor.timeout=60 --to notebook --execute --inplace \""+out_ipynb+"\"")