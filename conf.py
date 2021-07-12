import agents_bar


# -- Project information -----------------------------------------------------

project = 'Agents Bar Docs'
copyright = '2021, Agents Bar Ltd'
author = 'Dawid Laszuk'

# The full version, including alpha/beta/rc tags
release = 'alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

autosectionlabel_prefix_document = True
napoleon_include_init_with_doc = True
autodoc_member_order ="bysource"

def setup (app):
    app.add_css_file('custom.css')

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# NOTE: All the lines are after this are the theme-specific ones. These are
#       written as part of the site generation pipeline for this project.
# !! MARKER !!
import sphinx_theme
html_theme = "stanford_theme"
html_static_path = ['_static']
html_title = project
html_logo = '_static/logo-filled.png'
# html_logo = '_static/logo-dark.png'

html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}

#html_context = {
#    'display_github': True, # Integrate Gitlab
#    #'gitlab_host': 'gitlab.audeering.com',
#    'github_user': 'laszukdawid', # Username
#    'github_repo': 'ai-traineree', # Repo name
#    'github_version': 'master', # Branch
#    'conf_py_path': '/docs/', # Path in the checkout to the docs root
#}
