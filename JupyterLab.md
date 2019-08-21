Jupyter Lab Setup
=================


## System
Make sure that wasm is registered as a mime type. If not, register it:
```
echo "application/wasm      wasm" | sudo tee -a /etc/mime.types
```

Install nodejs to have access to jupyter lab extensions configuration : https://nodejs.org/en/download/package-manager/


## Virtualenv

Matplotlib widget:

```
pip install ipympl jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyter-matplotlib
```

Git plugin:
```
jupyter labextension install @jupyterlab/git
pip install --upgrade jupyterlab-git
jupyter serverextension enable --py jupyterlab_git
```

Diagrams:
```
jupyter labextension install @agoose77/jupyterlab-markup
```

Pretty Plotly Dash (for R):
```
pip install jupyterlab-dash==0.1.0a3
jupyter labextension install jupyterlab-dash@0.1.0-alpha.3
```

Diagrams from markdown in Jupyter notebook: https://github.com/jupyter/notebook/issues/2300

## TODO : bokeh ?
