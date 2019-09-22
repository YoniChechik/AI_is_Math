import os
import shutil
def build_from_site_metadata():

    #=== get all git class dirs - starting with "c_"
    cwd = os.getcwd()
    git_main_dirs_cwd = os.path.abspath(os.path.join(cwd, ".."))
    git_class_subdirs = [x for x in os.listdir(
        git_main_dirs_cwd) if x.startswith("c_")]

    pages_path = os.path.join(git_main_dirs_cwd,"docs","pages")

    # === build main headers
    main_toc_fp = os.path.join(pages_path, "toc.md")
    with open(main_toc_fp, "w+") as f:
        f.write(main_toc_header())

    main_index_fp = os.path.abspath(os.path.join(pages_path,"..", "index.html"))
    with open(main_index_fp, "w+") as f:
        f.write(main_index_header())

    # ==== run on all class dirs
    for dir_name in git_class_subdirs:
        fp = os.path.join(git_main_dirs_cwd, dir_name,"site_metadata")

        if not os.path.exists(fp):
            continue

        # ==== title name
        title = " ".join(dir_name.split("_")[2:])
        title = title[0].upper() + title[1:]

        # ==== dir in pages
        pages_class_dir_path = os.path.join(pages_path,dir_name)
        if not os.path.exists(pages_class_dir_path):
            os.mkdir(pages_class_dir_path)
        
        # === add bigimg to pages
        bigimg_path_pages = ""
        for fn in os.listdir(fp):
            if 'bigimg' in fn:
                # === copy img
                bigimg_path = os.path.join(fp,fn)
                bigimg_path_pages = os.path.join(pages_path,dir_name,fn)
                shutil.copyfile(bigimg_path,bigimg_path_pages)

                # === get shorten path
                bigimg_path_pages = os.sep +"pages" + bigimg_path_pages.split("pages")[1]

        # === run on all metadata files
        for meta_file in os.listdir(fp):
            if meta_file.endswith(".md"):
                
                # === build subtitle
                subtitle = " ".join(meta_file.split("_"))[:-3] # also remove ".md"
                subtitle = subtitle[0].upper() + subtitle[1:]
                
                # === copy orig file to pages and add header
                meta_file_path = os.path.join(fp,meta_file)
                with open(meta_file_path, 'r') as original:
                    meta_file_data = original.read()
                header_and_data = header_builder(title,subtitle,bigimg_path_pages) + meta_file_data
                meta_file_pages_path = os.path.join(pages_class_dir_path,meta_file)
                with open(meta_file_pages_path, 'w+') as modified:
                    modified.write(header_and_data)
                
                # ==== update main toc
                if meta_file == "table_of_contents.md":
                    with open(main_toc_fp, "a+") as f:
	                    f.write(meta_file_data+"\n\n")
                    url_toc = os.sep +"pages" + meta_file_pages_path.split("pages")[1][:-3] + os.sep

        # === build hover of index.html
        with open(main_index_fp, "a+") as f:
	        f.write(html_float_bar(url_toc,bigimg_path_pages,title))

            
def header_builder(title,subtitle,bigimg_path):
    # tamplate:
    # ---
    # title: CV & Python basics
    # subtitle: Table of contents
    # bigimg: /pages/c_01_basic_CV_and_python/intro.jpg
    # ---
    header = "---\n"
    header += "title: "+ title+"\n"
    header += "subtitle: "+ subtitle+"\n"
    header += "bigimg: "+ bigimg_path+"\n"
    header += "---\n\n"
    return header

def html_float_bar(url_content,url_image,title):
	html_str = ("\n"
                "<div class=\"mycont\">\n"
                "   <a href=\"{}\"><img class=\"hoverImages\" src=\"{}\">\n"
                "	<div class=\"bottom-left\"> \n"
                "		<h1>{}</h1>\n"
                "	</div>\n"
                "</div>\n").format(url_content, url_image, title)
	return html_str

def main_toc_header():
    # ==== start of main toc
    main_toc = ("---\n"
                "title: Course syllabus\n"
                "bigimg: /img/FedTech-ComputerVision.jpg\n"
                "---\n\n")
    return main_toc

def main_index_header():
    # === build start of main index
    with open("hover_main.css") as f:
        lines_arr = f.readlines()
    hover_main_css = "".join(lines_arr)

    main_index = ("---\n"
            "title: AI is Math\n"
            "subtitle: This is my computer vision course site. Why? Because it's awesome\n"
            "bigimg: /img/FedTech-ComputerVision.jpg\n"
            "---\n"
            "<style>\n"
            "{}\n"
            "</style>\n\n").format(hover_main_css)
    return main_index

if __name__ == "__main__":
    build_from_site_metadata()

