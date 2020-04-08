import json
import os

header_comment1 = '#%%'
header_comment2 = '# %%'


def _py2nb(py_str):

    cells = []
    chunks = py_str.replace(
        header_comment2, header_comment1).split(header_comment1)

    for chunk in chunks:
        if chunk == '':
            continue

        # if "[markdown]" in first_line:
        if "[markdown]" in chunk[:chunk.find(os.linesep)]:
            cell_type = 'markdown'
            chunk = chunk.replace("\n# ", "\n#").replace("\n#", "\n")
        else:
            cell_type = 'code'

        # remove "#%% ..." OR "#%% [markdown] ..." line
        chunk = chunk[chunk.find("\n")+1:]

        cell = {
            'cell_type': cell_type,
            'metadata': {},
            'source': chunk.splitlines(keepends=True),
        }

        if cell_type == 'code':
            cell.update({'outputs': [], 'execution_count': None})

        cells.append(cell)

    notebook = {
        'cells': cells,
        'metadata': {
            'language_info': {
                'codemirror_mode': {'name': 'ipython', 'version': 3},
                'file_extension': '.py',
                'mimetype': 'text/x-python',
                'name': 'python',
                'nbconvert_exporter': 'python',
                'pygments_lexer': 'ipython3',
                'version': '3'}},
        'nbformat': 4,
        'nbformat_minor': 2
    }

    return notebook


def _convert(in_file, out_file):
    with open(in_file, 'r', encoding='utf-8') as f:
        py_str = f.read()
    notebook = _py2nb(py_str)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)


def py2ipynb(py_fn, ipynb_fn):
    _convert(py_fn, ipynb_fn)


if __name__ == '__main__':
    out_file = "test2.ipynb"
    # py2ipynb(
    #     r"C:\Users\jonathanch\Google Drive\cv course\code\edges\edge_detection.py", out_file)
    py2ipynb(r"C:\Users\chech\Google Drive\cv_course\git\basic_CV_and_python\raw\1_basic_python_tutorial.py", out_file)
    # os.system("jupyter nbconvert --to notebook --execute "+out_file)
