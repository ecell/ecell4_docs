import sys
import os

extensions = [
    'nbsphinx', 'sphinx.ext.autodoc', 'sphinx.ext.autosummary',
    'IPython.sphinxext.ipython_console_highlighting', 'IPython.sphinxext.ipython_directive',
    'numpydoc',
]

nbsphinx_prolog = r"""
{% set path = env.doc2path(env.docname, base=None).replace('\\', '/') %}

.. only:: html

   .. seealso::

      Hoge

      This page was generated from `{{ path }} <https://github.com/kaizu/ecell4_docs/blob/{{ env.config.release|e }}/en/{{ path|e }}>`

      Download the `Jupyter Notebook <https://jupyter.org/>`_ for this section: :download:`{{ path.rsplit('/', 1)[1] }} </{{ path.replace('_notebooks', '_downloads') }}>`

      .. image:: https://colab.research.google.com/assets/colab-badge.svg
         :target: https://colab.research.google.com/github/kaizu/ecell4_docs/blob/{{ env.config.release|e }}/en/{{ path|e }}
      .. image:: https://mybinder.org/badge_logo.svg
         :target: https://mybinder.org/v2/gh/kaizu/ecell4_docs/{{ env.config.release|e }}?filepath=en/{{ path|e }}

"""

nbsphinx_epilog = r""

templates_path = ['_templates']

master_doc = 'index'

project = u'E-Cell4'
copyright = u'2015-, E-Cell project'
author = u'Kazunari Kaizu'

version = '1.0.0'
release = 'latest'

language = None

exclude_patterns = ['_build', '**.ipynb_checkpoints']

pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

html_show_sourcelink = True

htmlhelp_basename = 'Testdoc'

latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     'papersize': 'letterpaper',
#     # The font size ('10pt', '11pt' or '12pt').
#     'pointsize': '10pt',
#     # Additional stuff for the LaTeX preamble.
#     'preamble': '',
#     # Latex figure (float) alignment
#     'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'Test.tex', u'Test Documentation', u'Test', 'manual'),
]

man_pages = [
    (master_doc, 'test', u'Test Documentation', [author], 1)
]

texinfo_documents = [
  (master_doc, 'Test', u'Test Documentation', author, 'Test', 'One line description of project.',
      'Miscellaneous'),
]

from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
    '.md': CommonMarkParser,
}
