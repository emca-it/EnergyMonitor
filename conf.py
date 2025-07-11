from datetime import datetime

# -- Project information -----------------------------------------------------

project = 'Energy Monitor'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinx_rtd_size',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

file_insertion_enabled = False

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'body_max_width': None,  # disables max-width, allows wider content
}

htmlhelp_basename = 'energymonitor'

# -- LaTeX output -------------------------------------------------------------

latex_documents = [
    ('index', 'energymonitor.tex', 'Energy Monitor Documentation', '', 'manual'),
]
