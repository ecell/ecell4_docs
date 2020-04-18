import sys
import os

extensions = [
    'nbsphinx', 'sphinx.ext.autodoc', 'sphinx.ext.autosummary',
    'IPython.sphinxext.ipython_console_highlighting', 'IPython.sphinxext.ipython_directive',
    'numpydoc',
]

templates_path = ['_templates']


# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}
.. raw:: html
    <div class="admonition note">
      <p>This page was generated from
        <a class="reference external" href="https://github.com/kaizu/ecell4_doc/blob/{{ env.config.release|e }}/{{ docname|e }}">{{ docname|e }}</a>.
        Interactive online version:
        <a href="https://mybinder.org/v2/gh/kaizu/ecell4_doc/{{ env.config.release|e }}?filepath={{ docname|e }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>.
      </p>
      <script>
        if (document.location.host) {
          var p = document.currentScript.previousSibling.previousSibling;
          var a = document.createElement('a');
          a.innerHTML = 'View in <em>nbviewer</em>';
          a.href = `https://nbviewer.jupyter.org/url${
            (window.location.protocol == 'https:' ? 's/' : '/') +
            window.location.host +
            window.location.pathname.slice(0, -4) }ipynb`;
          a.classList.add('reference');
          a.classList.add('external');
          p.appendChild(a);
          p.appendChild(document.createTextNode('.'));
        }
      </script>
    </div>
.. raw:: latex
    \nbsphinxstartnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{The following section was generated from
    \sphinxcode{\sphinxupquote{\strut {{ docname | escape_latex }}}} \dotfill}}
"""

master_doc = 'index'

project = u'E-Cell4'
copyright = u'2015-, E-Cell project'
author = u'Kazunari Kaizu'

version = '2.0.0'
release = '2.0.0'

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
