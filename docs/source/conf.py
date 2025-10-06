import os
import sys
sys.path.insert(0, os.path.abspath('..\\..'))

project = 'Fasta project'
copyright = '2025, Lubov'
author = 'Lubov'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon', 
    'sphinx.ext.viewcode']

language = 'ru'
html_theme = 'sphinx_rtd_theme'
