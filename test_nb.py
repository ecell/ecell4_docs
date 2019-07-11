import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test_en_tutotiral1():
    _exec_notebook('en/tutorials/tutorial1.ipynb')

def test_en_tutotiral2():
    _exec_notebook('en/tutorials/tutorial2.ipynb')

def test_en_tutotiral3():
    _exec_notebook('en/tutorials/tutorial3.ipynb')

def test_en_tutotiral4():
    _exec_notebook('en/tutorials/tutorial4.ipynb')

def test_en_tutotiral5():
    _exec_notebook('en/tutorials/tutorial5.ipynb')

def test_en_tutotiral6():
    _exec_notebook('en/tutorials/tutorial6.ipynb')

def test_en_tutotiral7():
    _exec_notebook('en/tutorials/tutorial7.ipynb')

def test_en_tutotiral8():
    _exec_notebook('en/tutorials/tutorial8.ipynb')

def test_en_tutotiral9():
    _exec_notebook('en/tutorials/tutorial9.ipynb')

def test_en_tutotiral10():
    _exec_notebook('en/tutorials/tutorial10.ipynb')

def test_ja_tutotiral1():
    _exec_notebook('ja/tutorial1-ja.ipynb')

def test_ja_tutotiral2():
    _exec_notebook('ja/tutorial2-ja.ipynb')

def test_ja_tutotiral3():
    _exec_notebook('ja/tutorial3-ja.ipynb')

def test_ja_tutotiral4():
    _exec_notebook('ja/tutorial4-ja.ipynb')

def test_ja_tutotiral5():
    _exec_notebook('ja/tutorial5-ja.ipynb')

def test_ja_tutotiral6():
    _exec_notebook('ja/tutorial6-ja.ipynb')

def test_ja_tutotiral7():
    _exec_notebook('ja/tutorial7-ja.ipynb')

def test_ja_tutotiral8():
    _exec_notebook('ja/tutorial8-ja.ipynb')

def test_ja_tutotiral9():
    _exec_notebook('ja/tutorial9-ja.ipynb')

def test_ja_tutotiral10():
    _exec_notebook('ja/tutorial10-ja.ipynb')

