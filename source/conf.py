# -*- coding: utf-8 -*-

import os
import sys
#import xml.etree.ElementTree as etree

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
]

#extlinks = {
#    'roswiki': ('http://wiki.ros.org/%s', ''),
#}

source_suffix = '.rst'
master_doc = 'index'

project = u'Documentation'
copyright = u'2022, Clearpath Robotics'

# Get version number from package.xml.
#tree = etree.parse('../package.xml')
#version = tree.find("version").text
#release = version
release = u'0.0.1'

html_theme = 'theme'
html_theme_path = ["."]

htmlhelp_basename = 'cpr_doc'
templates_path = ['./templates']
html_static_path = ['./theme/static']

html_sidebars = {
   '**': ['sidebartoc.html', 'sourcelink.html', 'searchbox.html']
}

#rst_prolog = """
#.. |ros_distro| replace:: melodic
#.. |ubuntu_distro| replace:: bionic
#"""
#.. ubuntu_distro: bionic

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo/clearpathlogo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'logo/favicon.ico'

# -- Options for LaTeX output ------------------------------------------------
latex_engine = "xelatex"
latex_docclass = {
   'howto': 'clearpath-latex/clearpath-manual',
   'manual': 'clearpath-latex/clearpath-manual',
}
latex_additional_files = []
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'CprDocumentation.tex', 'CPR documentation',
     'Rhys Faultless', 'manual'),
]
