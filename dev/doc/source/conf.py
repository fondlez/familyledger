#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Ledger documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 14 19:00:25 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import sphinx_bootstrap_theme
import sphinx_rtd_theme
from tqdm import tqdm

# from familyledger.version import __version__


sys.path.insert(0, os.path.abspath('../../../familyledger'))
sys.setrecursionlimit(1500)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [    
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo']
#    ,
#    'sphinx_rtd_theme',
#    'sphinx-prompt']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Family Ledger'
copyright = '2020, fondlez'
author = 'fondlez'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2.0'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    'familyledger/__pycache__',
    'familyledger/build',
    'familyledger/dist',
    'familyledger/share',
    'familyledger/remi',
    'familyledger/slpp',
    'setup.py',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = "Family Ledger Documentation"
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = 'bootstrap'
# html_theme_path = ['../_themes']
html_theme_path = ['../_themes'] + sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {'nosidebar': True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Ledgerdoc'

# Remove permalinks.
html_add_permalinks = ""


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Ledger.tex', 'Family Ledger Documentation',
     'fondlez', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_images/logo.png'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ledger', 'Family Ledger Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Ledger', 'Family Ledger Documentation',
     author, 'Ledger', 'World of Warcraft account item data viewer',
     'Miscellaneous'),
]




# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

def setup(app):
    app.add_stylesheet('cli.css')
    # Ref: https://chrisdown.name/2015/09/20/removing-namedtuple-docstrings-from-sphinx.html
    app.connect('autodoc-process-docstring', no_namedtuple_attrib_docstring)

# Ref: https://chrisdown.name/2015/09/20/removing-namedtuple-docstrings-from-sphinx.html
def no_namedtuple_attrib_docstring(app, what, name, obj, options, lines):
    is_namedtuple_docstring = (
        len(lines) == 1 and lines[0].startswith('Alias')
    )
    if is_namedtuple_docstring:
        # We don't return, so we need to purge in-place
        del lines[:]
