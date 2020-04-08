import os
import shutil


def build_site(dirs):

    # === get all git class dirs - starting with "c_"
    cwd = os.getcwd()
    git_main_dirs_cwd = os.path.abspath(os.path.join(cwd, ".."))
    git_class_subdirs = [x for x in os.listdir(
        git_main_dirs_cwd) if x.startswith("c_")]
    git_class_subdirs.sort()

    pages_path = os.path.join(git_main_dirs_cwd, "docs", "pages")

    # === build index.html + toc headers + README
    main_toc_fp = os.path.join(pages_path, "toc.md")
    with open(main_toc_fp, "w+") as f:
        f.write(main_toc_header())

    main_index_fp = os.path.abspath(os.path.join(pages_path, "..", "index.html"))
    with open(main_index_fp, "w+") as f:
        f.write(main_index_header())

    readme_fp = os.path.join(git_main_dirs_cwd, "README.md")
    with open(readme_fp, "w+") as f:
        f.write(build_readme())

    # ==== run on all class dirs
    for dir_name in git_class_subdirs:
        fp = os.path.join(git_main_dirs_cwd, dir_name, "site_metadata")

        if not os.path.exists(fp):
            continue

        # ==== title name
        title = " ".join(dir_name.split("_")[2:])
        title = title[0].upper() + title[1:]

        # ==== dir in pages
        pages_class_dir_path = os.path.join(pages_path, dir_name)
        if not os.path.exists(pages_class_dir_path):
            os.mkdir(pages_class_dir_path)

        # === add bigimg to pages
        bigimg_path_pages = ""
        for fn in os.listdir(fp):
            if 'bigimg' in fn:
                # === copy img
                bigimg_path = os.path.join(fp, fn)
                bigimg_path_pages = os.path.join(pages_path, dir_name, fn)
                shutil.copyfile(bigimg_path, bigimg_path_pages)

                # === get shorten path
                bigimg_path_pages = os.sep + "pages" + bigimg_path_pages.split("pages")[1]

        # === run on all metadata files
        for meta_file in os.listdir(fp):
            if meta_file.endswith(".md"):

                # === build subtitle
                subtitle = " ".join(meta_file.split("_"))[:-3]  # also remove ".md"
                subtitle = subtitle[0].upper() + subtitle[1:]

                # === copy orig file to pages and add header
                meta_file_path = os.path.join(fp, meta_file)
                with open(meta_file_path, 'r') as original:
                    meta_file_data = original.read()
                header_and_data = header_builder(title, subtitle, bigimg_path_pages) + meta_file_data
                meta_file_pages_path = os.path.join(pages_class_dir_path, meta_file)
                with open(meta_file_pages_path, 'w+') as modified:
                    modified.write(header_and_data)

                # ==== update main toc
                if meta_file == "table_of_contents.md":
                    with open(main_toc_fp, "a+") as f:
                        f.write(meta_file_data+"\n\n")
                    url_toc = os.sep + "pages" + meta_file_pages_path.split("pages")[1][:-3] + os.sep

                    # ==== update readme
                    readme_class_text = meta_file_data.replace("##", "###").replace(
                        "/pages/", "https://www.aiismath.com/pages/")

                    with open(readme_fp, "a+") as f:
                        f.write(readme_class_text+"\n\n")

        # ==== build hover of index.html
        with open(main_index_fp, "a+") as f:
            f.write(html_float_bar(url_toc, bigimg_path_pages, title))

        # ==== build notebooks html
        class_dir = os.path.join(git_main_dirs_cwd, dir_name)
        if class_dir in dirs:
            for ipynb_file in os.listdir(class_dir):
                if ipynb_file.endswith(".ipynb"):
                    ipynb_file_no_ext = ipynb_file.split(".")[0]
                    ipynb_fp = os.path.join(class_dir, ipynb_file)
                    notebook_html_path = os.path.join(pages_class_dir_path, ipynb_file_no_ext+"_nb.html")

                    # ==== convert ipynb to html
                    os.system("jupyter nbconvert --ExecutePreprocessor.timeout=60 --template basic --to html  " +
                              ipynb_fp+" --output "+notebook_html_path)
                    with open(notebook_html_path, "r+") as f:
                        lines_arr = f.readlines()
                    # ===== deal with html
                    for i, line in enumerate(lines_arr):
                        if "class=\"anchor-link\"" in line:
                            # remove anchor symbol
                            line = line.replace("&#182;", "")
                            lines_arr[i] = line
                        if "<h1 id=" in line:
                            # remove h1 - leave the main title as h1
                            line = line.replace("<h1", "<h2")
                            line = line.replace("</h1>", "</h2>")
                            lines_arr[i] = line

                    nb_data = "".join(lines_arr)

                    # ==== for plotly: handle `iframe_figures` dir
                    iframe_figures_path = os.path.join(class_dir, 'iframe_figures')
                    if os.path.exists(iframe_figures_path):
                        # delete old dir
                        old_iframe_dir_path = os.path.join(pages_class_dir_path, 'iframe_figures')
                        if os.path.exists(old_iframe_dir_path):
                            shutil.rmtree(os.path.join(pages_class_dir_path, 'iframe_figures'))
                        # change path in nb_data
                        nb_data = nb_data.replace('iframe_figures', '/pages/'+dir_name+'/iframe_figures')
                        # move new dir to place
                        shutil.move(iframe_figures_path, pages_class_dir_path)

                    # ==== write header + data
                    subtitle = " ".join(ipynb_file_no_ext.split("_"))
                    subtitle = subtitle[0].upper() + subtitle[1:] + " notebook"
                    with open(notebook_html_path, "w+") as f:
                        f.write(header_builder(title, subtitle, bigimg_path_pages, layout="notebook"))
                        f.write(nb_data)


def header_builder(title, subtitle, bigimg_path, layout="page"):
    # tamplate:
    # ---
    # title: CV & Python basics
    # subtitle: Table of contents
    # bigimg: /pages/c_01_intro_to_CV_and_Python/intro.jpg
    # ---

    bigimg_path = bigimg_path.replace("\\", "/")  # some kind of weird bug...

    header = ("---\n"
              "title: {}\n"
              "subtitle: {}\n"
              "bigimg: {}\n"
              "share-img: https://raw.githubusercontent.com/YoniChechik/AI_is_Math/master/docs{}\n"
              "layout: {}\n"
              "---\n\n").format(title, subtitle, bigimg_path, bigimg_path, layout)
    return header


def build_readme():
    readme_text_start = (
        "# AI is Math\n"
        "**Check out my course site**: [AIisMath.com](https://AIisMath.com)\n"
        "\n"
        "This is my CV course raw data git repo - you can see the raw .py/ .ppt files here.\n"
        "\n"
        "## Course TOC\n")
    return readme_text_start


def html_float_bar(url_content, url_image, title):
    html_str = ("\n"
                "<div class=\"mycont\">\n"
                "   <a href=\"{0}\" aria-label=\"{2}\" ><img class=\"hoverImages\" src=\"{1}\" alt=\"{2}\">\n"
                "	<div class=\"yoni-bottom-left\"> \n"
                "		<h2>{2}</h2>\n"
                "	</div>\n"
                "</div>\n").format(url_content, url_image, title)
    return html_str


def main_toc_header():
    # ==== start of main toc
    main_toc = ("---\n"
                "title: Course syllabus\n"
                "bigimg: /img/FedTech-ComputerVision.jpg\n"
                "share-img: https://raw.githubusercontent.com/YoniChechik/"
                "AI_is_Math/master/docs/img/FedTech-ComputerVision.jpg\n"
                "---\n\n")
    return main_toc


def main_index_header():
    # === build start of main index
    main_index = ("---\n"
                  "title: AI is Math\n"
                  "subtitle: AI is Math is my computer vision course site, and yes- we also have neural networks\n"
                  "bigimg: /img/FedTech-ComputerVision.jpg\n"
                  "share-img: https://raw.githubusercontent.com/YoniChechik/"
                  "AI_is_Math/master/docs/img/FedTech-ComputerVision.jpg\n"
                  "css: \"/css/hover_main.css\"\n"
                  "---\n")
    return main_index


if __name__ == "__main__":
    build_site()
