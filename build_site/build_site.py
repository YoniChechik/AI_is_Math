import os

toc = """---
title: Course syllabus
bigimg: /img/FedTech-ComputerVision.jpg
---\n
"""

with open("hover_main.css") as f:
	lines_arr = f.readlines()
hover_main_css = "".join(lines_arr)

main = """---
title: AI is Math
subtitle: "This is my computer vision course site. Why? Because it's awesome"
bigimg: /img/FedTech-ComputerVision.jpg
---
<style>
{}
</style>
""".format(hover_main_css)


def html_float_bar(url_content,url_image,title):
	html_str = """\n
<div class="mycont">
		<a href="{}"><img class="hoverImages" src="{}">
		<div class="bottom-left"> 
				<h1>{}</h1>
		</div>
</div>
	""".format(url_content,url_image,title)
	return html_str


pages_path = os.path.join("..", "docs", "pages")
subdirs = os.listdir(pages_path)
subdirs.sort()
for subdir in subdirs:
	if not subdir.startswith("p_"):
		continue
	fp = os.path.join(pages_path, subdir)

	content_path = os.path.join(fp, "content.md")
	with open(content_path) as f:
		lines_arr = f.readlines()
	lines = "".join(lines_arr)

	# ==== build toc
	toc += lines.split("---\n")[-1]+"\n"

	# ===== build main
	url_content = "\\"+"\\".join(content_path.split("\\")[2:])[:-3]+"\\"
	url_image = [line for line in lines_arr if line.startswith("bigimg:")][0].split("bigimg:")[-1].split()[-1]
	title = " ".join([line for line in lines_arr if line.startswith("title:")][0].split("title:")[-1].split())

	main+=html_float_bar(url_content,url_image,title)


with open(os.path.join(pages_path, "toc.md"), "w+") as f:
	f.write(toc)
with open(os.path.join(pages_path,"..", "index.html"), "w+") as f:
	f.write(main)